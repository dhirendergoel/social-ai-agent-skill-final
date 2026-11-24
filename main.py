#!/usr/bin/env python3
"""
Social AI Agent Skill — Main CLI Entry Point
Run the full multi-agent social media automation pipeline.

Usage:
  python main.py --task "Create content for my fitness brand" --platforms instagram tiktok
  python main.py --config my_campaign.yaml
  python main.py --mode daily
"""

import os
import sys
import json
import yaml
import argparse
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(f"logs/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
    ],
)
logger = logging.getLogger(__name__)

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent / "tools"))


def run_full_pipeline(
    topic: str,
    platforms: list,
    brand_voice: str = "casual and engaging",
    niche: str = "",
    num_posts: int = 5,
    auto_publish: bool = False,
    output_dir: str = "output",
):
    """Run the complete multi-agent content pipeline."""
    
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    
    console = Console()
    
    console.print(Panel.fit(
        "[bold cyan]🤖 Social AI Agent Skill[/bold cyan]\n"
        f"Topic: {topic}\n"
        f"Platforms: {', '.join(platforms)}\n"
        f"Mode: {'Auto-publish' if auto_publish else 'Draft (review before publish)'}",
        border_style="cyan"
    ))
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    results = {}
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        
        # Phase 1: Content Generation
        task = progress.add_task("🔬 Research Agent: Analyzing trends...", total=None)
        try:
            from content_generator import AIContentGenerator, ContentRequest
            generator = AIContentGenerator()
            
            request = ContentRequest(
                topic=topic,
                platforms=platforms,
                brand_voice=brand_voice,
                niche=niche or topic,
                num_posts=num_posts,
            )
            
            progress.update(task, description="✍️ Content Agent: Creating posts...")
            content_package = generator.generate_post_package(request)
            results["content"] = content_package
            
            # Save content
            content_path = f"{output_dir}/content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(content_path, "w") as f:
                json.dump(content_package, f, indent=2)
            
            progress.update(task, description="🎨 Creative Agent: Generating reel scripts...")
            reel_script = generator.generate_reel_script(topic, duration=60)
            results["reel_script"] = reel_script
            
            progress.update(task, description="📅 Scheduler Agent: Planning schedule...")
            calendar = generator.generate_content_calendar(topic, duration_days=7, platforms=platforms)
            results["calendar"] = calendar
            
        except Exception as e:
            logger.error(f"Content generation failed: {e}")
            console.print(f"[red]❌ Content generation error: {e}[/red]")
            return results
        
        progress.update(task, description="✅ Content package ready!")
        progress.stop_task(task)
    
    # Display results
    posts = content_package.get("content_package", {}).get("posts", [])
    console.print(f"\n[green]✅ Generated {len(posts)} posts across {len(platforms)} platforms[/green]")
    console.print(f"[dim]Saved to: {content_path}[/dim]")
    
    # Phase 2: Publishing (if auto_publish enabled)
    if auto_publish:
        console.print("\n[yellow]📢 Publishing Agent: Starting publication...[/yellow]")
        try:
            from publisher import MultiPlatformPublisher, Post
            
            publisher = MultiPlatformPublisher()
            publish_posts = []
            
            for p in posts:
                post = Post(
                    post_id=f"{topic[:20]}_{p.get('platform')}_{datetime.now().timestamp()}",
                    platform=p.get("platform", "instagram"),
                    post_type=p.get("type", "post"),
                    caption=p.get("full_caption", p.get("body", "")),
                    hashtags=p.get("hashtags", []),
                )
                publish_posts.append(post)
            
            publish_results = publisher.publish_all(publish_posts)
            summary = publisher.get_summary()
            results["publish_results"] = summary
            
            console.print(f"[green]✅ Published: {summary['successful']}/{summary['total_attempted']} posts[/green]")
            
        except Exception as e:
            logger.error(f"Publishing failed: {e}")
            console.print(f"[red]❌ Publishing error: {e}[/red]")
    else:
        console.print("\n[dim]ℹ️  Auto-publish is OFF. Review content in output/ before publishing.[/dim]")
        console.print(f"[dim]To publish: python tools/publisher.py --input {content_path}[/dim]")
    
    return results


def run_daily_mode(config_path: str = "configs/content_rules.yaml"):
    """Run the daily content automation mode."""
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    brand = config.get("brand", {})
    posting = config.get("posting", {})
    
    active_platforms = [
        p for p, settings in posting.get("platforms", {}).items()
        if settings.get("enabled", False)
    ]
    
    logger.info(f"Daily mode: generating content for {active_platforms}")
    
    return run_full_pipeline(
        topic=f"daily content for {brand.get('name', 'your brand')}",
        platforms=active_platforms,
        brand_voice=config.get("voice", {}).get("tone", "casual"),
        auto_publish=posting.get("auto_publish", False),
    )


def main():
    parser = argparse.ArgumentParser(
        description="🤖 Social AI Agent Skill — Full social media automation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --topic "AI productivity tips" --platforms instagram x tiktok
  python main.py --topic "product launch" --platforms all --publish
  python main.py --mode daily
  python main.py --config my_campaign.yaml
        """
    )
    
    parser.add_argument("--topic", help="Content topic or campaign theme")
    parser.add_argument(
        "--platforms", nargs="+",
        choices=["instagram", "facebook", "x", "tiktok", "linkedin", "youtube", "threads", "all"],
        default=["instagram", "x", "tiktok"],
        help="Target platforms"
    )
    parser.add_argument("--voice", default="casual and engaging", help="Brand voice/tone")
    parser.add_argument("--niche", default="", help="Brand niche")
    parser.add_argument("--posts", type=int, default=5, help="Number of posts to generate")
    parser.add_argument("--publish", action="store_true", help="Auto-publish after generating")
    parser.add_argument("--mode", choices=["single", "daily", "weekly"], 
                        default="single", help="Run mode")
    parser.add_argument("--config", help="YAML config file for campaign")
    parser.add_argument("--output", default="output", help="Output directory")
    
    args = parser.parse_args()
    
    # Expand "all" platforms
    all_platforms = ["instagram", "facebook", "x", "tiktok", "linkedin", "threads"]
    platforms = all_platforms if "all" in args.platforms else args.platforms
    
    if args.mode == "daily":
        run_daily_mode()
    elif args.config:
        with open(args.config) as f:
            campaign = yaml.safe_load(f)
        run_full_pipeline(**campaign)
    else:
        if not args.topic:
            parser.error("--topic is required for single mode")
        
        run_full_pipeline(
            topic=args.topic,
            platforms=platforms,
            brand_voice=args.voice,
            niche=args.niche,
            num_posts=args.posts,
            auto_publish=args.publish,
            output_dir=args.output,
        )


if __name__ == "__main__":
    main()

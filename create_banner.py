"""
Banner generator for Learning Machines notebooks.
Style: "Final Hierarchical" - Minimalist, white background, with strong
typographic hierarchy to dominate notebook section headers.
"""

import matplotlib.pyplot as plt
from pathlib import Path
import base64
from io import BytesIO

# =============================================================================
# Brand colors (from mlone_theme.py notebook family)
# =============================================================================
FOREST = '#2D5A00'      # Dark anchor for main title
GREEN = '#4F9E00'       # Primary topic accent
SEAFOAM = '#3EB489'     # Light accent for separator line
GRAY = '#666666'        # Secondary text (metadata, subtitles)
WHITE = '#FFFFFF'       # Background

def create_banner(
    subtitle="Polynomial Regression",
    author="Gregory Wheeler",
    github_url="github.com/gw/learning-machines",
    figsize=(10, 2.0), # Increased height to accommodate larger title
    dpi=150
):
    """
    Create a minimalist typographic notebook header banner with strong hierarchy.
    """
    # Setup figure with white background
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)

    # Set figure bounds
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2.0) # Adjusted Y-limit for new height
    ax.axis('off')

    # =========================================================================
    # Typography & Layout
    # =========================================================================
    text_x = 0.4
    font_family = 'sans-serif'

    # 1. Main Title Block (Top Left)
    # -----------------------------------------------------------
    # Main Title: INCREASED from 24 to 32 for primary hierarchy
    ax.text(text_x, 1.55, "Learning Machines",
            fontsize=32, fontweight='bold', color=FOREST,
            verticalalignment='center', fontfamily=font_family)

    # Book Subtitle: Adjusted position
    ax.text(text_x, 1.15, "A Statistical Introduction",
            fontsize=18, color=GRAY, style='italic',
            verticalalignment='center', fontfamily=font_family)

    # 2. Separator Line
    # -----------------------------------------------------------
    # Moved down slightly
    ax.plot([text_x, 9.5], [0.9, 0.9], color=SEAFOAM, linewidth=1, zorder=1)

    # 3. Notebook Topic
    # -----------------------------------------------------------
    # Notebook Topic: fontsize 16 is now visually subordinate to the main title
    ax.text(text_x, 0.6, f"► {subtitle}",
            fontsize=16, color=GREEN,
            verticalalignment='center', fontfamily=font_family)

    # =========================================================================
    # Metadata (Bottom Right)
    # =========================================================================
    meta_text = f"{author}"
    if github_url:
        # Clean URL for display
        display_url = github_url.replace("https://", "").replace("http://", "")
        meta_text += f" · {display_url}"

    # Metadata: Adjusted position and slightly smaller font (11)
    ax.text(9.8, 0.2, meta_text,
            fontsize=11, color=GRAY,
            verticalalignment='center', horizontalalignment='right',
            fontfamily=font_family)

    plt.tight_layout(pad=0)
    return fig


def banner_to_base64(fig, format='png', dpi=150):
    """Convert matplotlib figure to base64 string for embedding."""
    buffer = BytesIO()
    # Ensure saved image has white background and no padding
    fig.savefig(buffer, format=format, dpi=dpi, bbox_inches='tight',
                pad_inches=0, facecolor=WHITE, edgecolor='none')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    return img_str


def generate_markdown_header(subtitle):
    """
    Generate complete markdown cell content with embedded banner.
    Defaults to hardcoded author/url for easy notebook usage.
    """
    fig = create_banner(subtitle=subtitle)
    b64 = banner_to_base64(fig)

    # Markdown with margin for spacing
    markdown = f'''<div style="margin-bottom: 32px;">
<img src="data:image/png;base64,{b64}"
     alt="Learning Machines: {subtitle}"
     style="width: 100%; max-width: 900px; border-radius: 2px;">
</div>
'''
    return markdown


if __name__ == "__main__":
    # Test output
    output_dir = Path("banner_output_final")
    output_dir.mkdir(exist_ok=True)

    topics = [
        "Polynomial Regression",
        "Gradient Descent",
        "Bayesian Inference"
    ]

    print("Generating final sample banners...")
    for topic in topics:
        fig = create_banner(subtitle=topic)
        filename = topic.lower().replace(" ", "_") + "_banner.png"
        filepath = output_dir / filename

        fig.savefig(filepath, dpi=150, bbox_inches='tight', pad_inches=0,
                    facecolor=WHITE, edgecolor='none')
        plt.close(fig)
        print(f"- Created: {filepath}")

    print(f"\nDone. Samples saved to ./{output_dir.name}/")
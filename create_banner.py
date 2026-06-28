"""
Banner generator for Learning Machines notebooks.
Matches the companion site's identity: Frankfurt-School blue wordmark, a red
circle mark (echoing the site navbar), Georgia serif (the site's Fraunces
fallback), and a sparing red accent. White background, strong hierarchy.
"""

import matplotlib.pyplot as plt
from pathlib import Path
import base64
from io import BytesIO

# =============================================================================
# Brand colors (aligned to the companion site / theme.scss)
# =============================================================================
FS_BLUE = '#31417A'     # Frankfurt School blue — wordmark + topic
RED     = '#E3120B'     # sharp accent — the brand circle (matches the navbar mark)
GRAY    = '#666666'     # secondary text (subtitle, metadata)
RULE    = '#D9D9D9'     # subtle separator
WHITE   = '#FFFFFF'     # background

FONT = 'Georgia'        # the site's serif fallback for the Fraunces wordmark


def create_banner(
    subtitle="Polynomial Regression",
    author="Gregory Wheeler",
    github_url="github.com/welr/learning_machines",
    figsize=(10, 2.0),
    dpi=150,
):
    """Create the notebook header banner, matched to the companion-site identity."""
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor(WHITE)
    ax.set_facecolor(WHITE)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2.0)
    ax.axis('off')

    left = 1.05  # left edge of the wordmark and everything beneath it

    # Brand mark: a red circle to the left of the wordmark (mirrors the navbar)
    ax.scatter([0.55], [1.52], s=470, color=RED, zorder=3, edgecolors='none')

    # Wordmark
    ax.text(left, 1.5, "Learning Machines",
            fontsize=32, fontweight='bold', color=FS_BLUE,
            verticalalignment='center', fontfamily=FONT)

    # Book subtitle
    ax.text(left, 1.08, "A Statistical Introduction",
            fontsize=18, color=GRAY, style='italic',
            verticalalignment='center', fontfamily=FONT)

    # Separator
    ax.plot([left, 9.5], [0.82, 0.82], color=RULE, linewidth=1, zorder=1)

    # Notebook topic: a small red dot + blue label (replaces the old green ►)
    ax.scatter([left + 0.07], [0.5], s=70, color=RED, zorder=3, edgecolors='none')
    ax.text(left + 0.30, 0.5, subtitle,
            fontsize=16, color=FS_BLUE,
            verticalalignment='center', fontfamily=FONT)

    # Metadata (bottom right)
    meta_text = f"{author}"
    if github_url:
        display_url = github_url.replace("https://", "").replace("http://", "")
        meta_text += f" · {display_url}"
    ax.text(9.7, 0.18, meta_text,
            fontsize=11, color=GRAY,
            verticalalignment='center', horizontalalignment='right',
            fontfamily=FONT)

    plt.tight_layout(pad=0)
    return fig


def banner_to_base64(fig, format='png', dpi=150):
    """Convert matplotlib figure to base64 string for embedding."""
    buffer = BytesIO()
    fig.savefig(buffer, format=format, dpi=dpi, bbox_inches='tight',
                pad_inches=0, facecolor=WHITE, edgecolor='none')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    return img_str


def generate_markdown_header(subtitle):
    """Generate the markdown cell content with the embedded banner."""
    fig = create_banner(subtitle=subtitle)
    b64 = banner_to_base64(fig)
    markdown = f'''<div style="margin-bottom: 32px;">
<img src="data:image/png;base64,{b64}"
     alt="Learning Machines: {subtitle}"
     style="width: 100%; max-width: 900px; border-radius: 2px;">
</div>
'''
    return markdown


if __name__ == "__main__":
    output_dir = Path("banner_output")
    output_dir.mkdir(exist_ok=True)
    for topic in ["Polynomial Regression", "Gradient Descent", "Capstone: Build a GPT"]:
        fig = create_banner(subtitle=topic)
        filepath = output_dir / (topic.lower().replace(" ", "_").replace(":", "") + "_banner.png")
        fig.savefig(filepath, dpi=150, bbox_inches='tight', pad_inches=0,
                    facecolor=WHITE, edgecolor='none')
        plt.close(fig)
        print(f"- Created: {filepath}")
    print(f"\nDone. Samples in ./{output_dir.name}/")

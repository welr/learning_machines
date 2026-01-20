"""
MLone Theme - Unified plotting utilities for Machine Learning textbook and notebooks.

This module provides:
- Unified color palette with Blue Family (book) and Green Family (notebooks)
- Helper functions for applying the Economist style
- Utilities for direct line labels, right-side y-axis, etc.
- Mode switching between book and notebook color cycles

Usage:
    import mlone_theme as mt
    import matplotlib.pyplot as plt

    plt.style.use('mlone_style.mplstyle')

    # For book figures (default)
    mt.set_book_mode()

    # For notebooks
    mt.set_notebook_mode()

    fig, ax = plt.subplots()
    ax.plot(x, y, color=mt.BLUE)
    mt.apply_economist_style(ax)
    mt.save_figure(fig, 'my_figure')
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

# =============================================================================
# UNIFIED COLOR PALETTE
# =============================================================================

# -----------------------------------------------------------------------------
# Blue Family (Book) - dark to light gradient
# -----------------------------------------------------------------------------
FS_BLUE = '#31417A'       # Dark anchor — headings, brand emphasis
BLUE = '#076FA1'          # Primary — first series in book figures
CYAN = '#2FC1D3'          # Light — second series in book figures

# -----------------------------------------------------------------------------
# Green Family (Notebooks) - dark to light gradient, converging toward teal
# -----------------------------------------------------------------------------
FOREST = '#2D5A00'        # Dark anchor — headings, brand emphasis
GREEN = '#4F9E00'         # Primary — first series in notebooks
SEAFOAM = '#3EB489'       # Light — second series in notebooks

# -----------------------------------------------------------------------------
# Shared Semantic Colors
# -----------------------------------------------------------------------------
RED = '#E3120B'           # Errors, warnings, test error
ORANGE = '#9E4F00'        # Caution, third accent

# -----------------------------------------------------------------------------
# Neutrals
# -----------------------------------------------------------------------------
BROWN = '#AD8C97'         # Muted accent, historical data
BROWN_DARK = '#7D3A46'    # Dark accent
GRAY = '#666666'          # Secondary text, baselines
GRAY_LIGHT = '#C7C9CB'    # Backgrounds, disabled states
GRID_COLOR = '#A8BAC4'    # Grid lines
TEXT_COLOR = '#333333'    # Primary text

# Legacy aliases for backward compatibility
BROWN_DARKER = BROWN_DARK
GRAY_DARKER = GRAY

# =============================================================================
# COLOR CYCLES
# =============================================================================

# Book mode: blue family first (Economist style)
BOOK_COLORS = [BLUE, CYAN, GREEN, SEAFOAM, RED, ORANGE, GRAY]
BOOK_COLORS_2 = [BLUE, CYAN]
BOOK_COLORS_3 = [BLUE, CYAN, RED]

# Notebook mode: green family first (computation emphasis)
NOTEBOOK_COLORS = [GREEN, SEAFOAM, BLUE, CYAN, RED, ORANGE, GRAY]
NOTEBOOK_COLORS_2 = [GREEN, SEAFOAM]
NOTEBOOK_COLORS_3 = [GREEN, SEAFOAM, RED]

# Active colors (default to book mode)
COLORS = BOOK_COLORS
COLORS_2 = BOOK_COLORS_2
COLORS_3 = BOOK_COLORS_3

# =============================================================================
# MODE SWITCHING
# =============================================================================

def set_notebook_mode():
    """
    Switch to notebook color cycle (green family first).

    Use this at the start of companion notebooks to signal "computation mode".
    The green→seafoam gradient parallels the book's blue→cyan gradient.

    Example:
        import mlone_theme as mt
        mt.set_notebook_mode()
    """
    global COLORS, COLORS_2, COLORS_3
    COLORS = NOTEBOOK_COLORS
    COLORS_2 = NOTEBOOK_COLORS_2
    COLORS_3 = NOTEBOOK_COLORS_3
    plt.rcParams['axes.prop_cycle'] = plt.cycler('color', NOTEBOOK_COLORS)


def set_book_mode():
    """
    Switch to book color cycle (blue family first).

    This is the default mode, matching the Economist-style figures in the textbook.
    Use this when generating figures for the PDF.

    Example:
        import mlone_theme as mt
        mt.set_book_mode()
    """
    global COLORS, COLORS_2, COLORS_3
    COLORS = BOOK_COLORS
    COLORS_2 = BOOK_COLORS_2
    COLORS_3 = BOOK_COLORS_3
    plt.rcParams['axes.prop_cycle'] = plt.cycler('color', BOOK_COLORS)


# =============================================================================
# STYLE APPLICATION
# =============================================================================

def apply_economist_style(ax, title=None, subtitle=None, y_label_right=True):
    """
    Apply Economist-style formatting to an axes object.

    This function applies additional styling beyond what the .mplstyle file provides,
    particularly for elements that need to be set after plotting.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to style
    title : str, optional
        Bold title text
    subtitle : str, optional
        Lighter subtitle text (placed below title)
    y_label_right : bool, default True
        Whether to place y-axis labels on the right side
    """
    # Ensure only bottom spine is visible
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_color('black')
    ax.spines['bottom'].set_linewidth(1.0)

    # Grid: horizontal only
    ax.yaxis.grid(True, color=GRID_COLOR, linewidth=0.5)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)

    # Y-axis on right side (Economist style)
    if y_label_right:
        ax.yaxis.tick_right()
        ax.yaxis.set_label_position('right')
        ax.tick_params(axis='y', left=False, right=False, labelleft=False, labelright=True)

    # X-axis ticks
    ax.tick_params(axis='x', bottom=True, top=False, direction='out', length=4)

    # Title and subtitle
    if title:
        ax.set_title(title, fontweight='bold', fontsize=18, loc='left', pad=12)
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, fontsize=14,
                color=GRAY, va='bottom', ha='left')


def setup_figure(figsize=(6.5, 4.5), style_path=None):
    """
    Create a figure with the MLone style applied.

    Parameters
    ----------
    figsize : tuple, default (6.5, 4.5)
        Figure size in inches
    style_path : str or Path, optional
        Path to mlone_style.mplstyle. If None, tries to find it automatically.

    Returns
    -------
    fig, ax : tuple
        Matplotlib figure and axes objects
    """
    # Try to apply style
    if style_path:
        plt.style.use(str(style_path))
    else:
        # Try common locations
        possible_paths = [
            Path(__file__).parent / 'mlone_style.mplstyle',
            Path.cwd() / 'mlone_style.mplstyle',
        ]
        for path in possible_paths:
            if path.exists():
                plt.style.use(str(path))
                break

    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax


# =============================================================================
# DIRECT LABELS (instead of legends)
# =============================================================================

def add_direct_label(ax, x, y, text, color, fontsize=12, ha='left', va='center',
                     offset=(5, 0), background=True):
    """
    Add a direct label to a line or point (Economist style - no legends).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to add the label to
    x, y : float
        Position for the label
    text : str
        Label text
    color : str
        Text color (usually matches the line color)
    fontsize : int, default 12
        Font size
    ha : str, default 'left'
        Horizontal alignment
    va : str, default 'center'
        Vertical alignment
    offset : tuple, default (5, 0)
        Offset in points (x, y) from the specified position
    background : bool, default True
        Whether to add a white background box (like geom_shadowtext)
    """
    bbox_props = None
    if background:
        bbox_props = dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor='none', alpha=0.8)

    ax.annotate(text, xy=(x, y), xytext=offset, textcoords='offset points',
                fontsize=fontsize, color=color, ha=ha, va=va,
                fontweight='normal', bbox=bbox_props)


def add_line_labels(ax, lines, labels, colors=None, position='end'):
    """
    Add labels directly to multiple lines.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes containing the lines
    lines : list of Line2D
        The line objects to label
    labels : list of str
        Labels for each line
    colors : list of str, optional
        Colors for each label (defaults to line colors)
    position : str, default 'end'
        Where to place labels: 'end', 'start', or 'middle'
    """
    for i, (line, label) in enumerate(zip(lines, labels)):
        xdata, ydata = line.get_xdata(), line.get_ydata()
        color = colors[i] if colors else line.get_color()

        if position == 'end':
            x, y = xdata[-1], ydata[-1]
            ha, offset = 'left', (8, 0)
        elif position == 'start':
            x, y = xdata[0], ydata[0]
            ha, offset = 'right', (-8, 0)
        else:  # middle
            mid = len(xdata) // 2
            x, y = xdata[mid], ydata[mid]
            ha, offset = 'center', (0, 10)

        add_direct_label(ax, x, y, label, color, ha=ha, offset=offset)


# =============================================================================
# FIGURE SAVING
# =============================================================================

def save_figure(fig, name, output_dir=None, formats=('pdf',), dpi=300):
    """
    Save figure to file(s) with proper settings for publication.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to save
    name : str
        Base filename (without extension)
    output_dir : str or Path, optional
        Output directory. Defaults to 'figures/' in current directory.
    formats : tuple, default ('pdf',)
        Output formats (e.g., ('pdf', 'png'))
    dpi : int, default 300
        Resolution for raster formats
    """
    if output_dir is None:
        output_dir = Path(__file__).parent / 'figures'
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    for fmt in formats:
        filepath = output_dir / f'{name}.{fmt}'
        fig.savefig(filepath, format=fmt, dpi=dpi, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f'Saved: {filepath}')


# =============================================================================
# SPECIALIZED PLOT FUNCTIONS
# =============================================================================

def scatter_with_border(ax, x, y, color=BLUE, size=60, border_color='white',
                        border_width=1.5, **kwargs):
    """
    Create a scatter plot with white-bordered points (Economist style).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to plot on
    x, y : array-like
        Data coordinates
    color : str, default BLUE
        Fill color for points
    size : int, default 60
        Point size
    border_color : str, default 'white'
        Edge color
    border_width : float, default 1.5
        Edge width
    **kwargs : dict
        Additional arguments passed to ax.scatter

    Returns
    -------
    PathCollection
        The scatter plot object
    """
    return ax.scatter(x, y, c=color, s=size, edgecolors=border_color,
                      linewidths=border_width, zorder=3, **kwargs)


def line_with_points(ax, x, y, color=BLUE, linewidth=2, point_size=60,
                     label=None, **kwargs):
    """
    Create a line plot with scatter points overlaid (Economist style).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to plot on
    x, y : array-like
        Data coordinates
    color : str, default BLUE
        Line and point color
    linewidth : float, default 2
        Line width
    point_size : int, default 60
        Point size
    label : str, optional
        Label for the series
    **kwargs : dict
        Additional arguments

    Returns
    -------
    tuple
        (Line2D, PathCollection) - the line and scatter objects
    """
    line, = ax.plot(x, y, color=color, linewidth=linewidth, zorder=2, **kwargs)
    scatter = scatter_with_border(ax, x, y, color=color, size=point_size)
    return line, scatter


# =============================================================================
# DIAGRAM HELPERS (for architecture figures)
# =============================================================================

def draw_box(ax, xy, width, height, text='', color=BLUE, text_color='white',
             fontsize=11, alpha=1.0, rounded=True):
    """
    Draw a labeled box (for architecture diagrams).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to draw on
    xy : tuple
        (x, y) position of bottom-left corner
    width, height : float
        Box dimensions
    text : str
        Text to display inside the box
    color : str
        Box fill color
    text_color : str
        Text color
    fontsize : int
        Font size for text
    alpha : float
        Transparency
    rounded : bool
        Whether to use rounded corners

    Returns
    -------
    FancyBboxPatch
        The box patch object
    """
    if rounded:
        box = FancyBboxPatch(xy, width, height,
                             boxstyle='round,pad=0.02,rounding_size=0.1',
                             facecolor=color, edgecolor='none', alpha=alpha)
    else:
        box = mpatches.Rectangle(xy, width, height, facecolor=color,
                                  edgecolor='none', alpha=alpha)
    ax.add_patch(box)

    if text:
        cx = xy[0] + width / 2
        cy = xy[1] + height / 2
        ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize,
                color=text_color, fontweight='bold')

    return box


def draw_arrow(ax, start, end, color=GRAY, width=0.02, head_width=0.06,
               head_length=0.03, curved=False):
    """
    Draw an arrow between two points (for architecture diagrams).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to draw on
    start, end : tuple
        (x, y) positions for arrow start and end
    color : str
        Arrow color
    width : float
        Arrow shaft width
    head_width : float
        Arrow head width
    head_length : float
        Arrow head length
    curved : bool
        Whether to use a curved arrow

    Returns
    -------
    FancyArrowPatch or Arrow
        The arrow object
    """
    if curved:
        arrow = FancyArrowPatch(start, end, connectionstyle='arc3,rad=0.3',
                                arrowstyle='->', mutation_scale=15,
                                color=color, linewidth=2)
        ax.add_patch(arrow)
        return arrow
    else:
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        arrow = ax.arrow(start[0], start[1], dx, dy, width=width,
                         head_width=head_width, head_length=head_length,
                         fc=color, ec=color, length_includes_head=True)
        return arrow


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def remove_legend(ax):
    """Remove the legend from an axes."""
    legend = ax.get_legend()
    if legend:
        legend.remove()


def set_axis_format(ax, x_format=None, y_format=None):
    """
    Set number formatting for axis tick labels.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to format
    x_format : str, optional
        Format string for x-axis (e.g., '%.1f', '%d')
    y_format : str, optional
        Format string for y-axis
    """
    from matplotlib.ticker import FormatStrFormatter
    if x_format:
        ax.xaxis.set_major_formatter(FormatStrFormatter(x_format))
    if y_format:
        ax.yaxis.set_major_formatter(FormatStrFormatter(y_format))


def set_clean_ticks(ax, x_ticks=None, y_ticks=None, x_labels=None, y_labels=None):
    """
    Set clean, minimal tick marks (Economist style).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to modify
    x_ticks, y_ticks : array-like, optional
        Tick positions
    x_labels, y_labels : array-like, optional
        Custom tick labels
    """
    if x_ticks is not None:
        ax.set_xticks(x_ticks)
    if y_ticks is not None:
        ax.set_yticks(y_ticks)
    if x_labels is not None:
        ax.set_xticklabels(x_labels)
    if y_labels is not None:
        ax.set_yticklabels(y_labels)

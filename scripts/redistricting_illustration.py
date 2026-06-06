import matplotlib.pyplot as plt
import matplotlib.patches as patches


def get_district(row, col, case):
    if case == "simple":
        return 0 if row < 5 else 1
    else:
        if row == 0:
            return 0
        elif row == 9:
            return 1
        else:
            return col % 2  # alternating columns in middle rows


def count_border_edges(case):
    N = 10
    count = 0
    for row in range(N):
        for col in range(N):
            d = get_district(row, col, case)
            if col + 1 < N and get_district(row, col + 1, case) != d:
                count += 1
            if row + 1 < N and get_district(row + 1, col, case) != d:
                count += 1
    return count


def draw_grid(ax, case, title):
    N = 10
    colors = {0: "white", 1: "#222222"}

    for row in range(N):
        for col in range(N):
            d = get_district(row, col, case)
            y = (N - 1 - row)
            rect = patches.Rectangle(
                (col, y), 1, 1,
                linewidth=0.4,
                edgecolor="#aaaaaa",
                facecolor=colors[d],
            )
            ax.add_patch(rect)

    tick = 0.2       # half-length of perpendicular tick
    lw_inner = 2.5
    lw_border = lw_inner * 1.6  # gray outline is proportionally thicker
    for row in range(N):
        for col in range(N):
            d = get_district(row, col, case)
            y = (N - 1 - row)
            # vertical border between col and col+1 → horizontal tick
            if col + 1 < N and get_district(row, col + 1, case) != d:
                x = col + 1
                cy = y + 0.5
                ax.plot([x - tick, x + tick], [cy, cy], color="#aaaaaa", linewidth=lw_border, solid_capstyle="round")
                ax.plot([x - tick, x + tick], [cy, cy], color="#1a6fdb", linewidth=lw_inner, solid_capstyle="round")
            # horizontal border between row and row+1 → vertical tick
            if row + 1 < N and get_district(row + 1, col, case) != d:
                bx = col + 0.5
                ax.plot([bx, bx], [y - tick, y + tick], color="#aaaaaa", linewidth=lw_border, solid_capstyle="round")
                ax.plot([bx, bx], [y - tick, y + tick], color="#1a6fdb", linewidth=lw_inner, solid_capstyle="round")

    edge_count = count_border_edges(case)
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"{title}\n{edge_count} border edges", fontsize=13, pad=8)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5))

draw_grid(ax1, "simple", "Compact District")
draw_grid(ax2, "gerrymandered", "Gerrymandered District")

plt.suptitle("Redistricting: Compact vs. Gerrymandered", fontsize=15, y=1.01)
plt.tight_layout()

import os
os.makedirs("static/images", exist_ok=True)
out_path = "static/images/redistricting_illustration.png"
plt.savefig(out_path, dpi=150, bbox_inches="tight", facecolor="white")
print(f"Saved to {out_path}")

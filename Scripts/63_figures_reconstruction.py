"""
63_figures_reconstruction.py
Figures for the reconstructed thesis. Reads the tables written by Scripts 61-62.
Palette: fixed categorical order (blue, orange, aqua, yellow) for the four
product groups; one axis per chart; legends plus direct labels.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent.parent
T = ROOT / "Outputs" / "generated_tables"
F = ROOT / "Outputs" / "generated_figures"
F.mkdir(parents=True, exist_ok=True)
COL = {"energy": "#2a78d6", "metals_ores": "#eb6834", "agrifood": "#1baf7a", "other": "#eda100"}
LAB = {"energy": "Energy (HS27)", "metals_ores": "Metals and ores", "agrifood": "Agri-food (HS01-24)",
       "other": "Other goods"}
INK, MUTED = "#0b0b0b", "#52514e"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": MUTED,
                     "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": "#e6e5e0", "grid.linewidth": 0.6})
SRC = "Source: UN Comtrade (HS-2, public API); author's calculations."


def foot(fig, extra=""):
    fig.text(0.01, 0.005, SRC + (" " + extra if extra else ""), fontsize=6.5, color=MUTED)


# Fig R1: composition of Kazakhstan's exports to China (China-reported, complete series)
c = pd.read_csv(T / "composition_kz_exports_to_china.csv")
m = c[c["source"] == "cn_m_kaz"].set_index("year")
fig, ax = plt.subplots(figsize=(7.2, 3.6))
bottom = np.zeros(len(m))
for g in ["energy", "metals_ores", "agrifood", "other"]:
    ax.bar(m.index, m[f"{g}_bn"], bottom=bottom, color=COL[g], label=LAB[g], width=0.8,
           edgecolor="white", linewidth=1)
    bottom += m[f"{g}_bn"].values
ax.set_ylabel("USD billion (current)")
ax.set_title("Kazakhstan's exports to China by product group, China-reported imports (CIF)", fontsize=9.5)
ax.legend(frameon=False, fontsize=8, ncol=4, loc="upper left")
ax.set_ylim(0, 19)
ax.text(2006, 0.3, "n/a", fontsize=7, color=MUTED, ha="center")
ax.set_xticks(range(2005, 2025, 2))
foot(fig)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(F / "fig_r1_composition_china.png", dpi=200); plt.close(fig)

# Fig R2: China's share of Kazakhstan's exports by group (KZ-reported)
s = pd.read_csv(T / "china_share_by_group.csv").set_index("year")
fig, ax = plt.subplots(figsize=(7.2, 3.6))
for g in ["energy", "metals_ores", "agrifood", "other"]:
    seg = s[g]
    for part in (seg[seg.index <= 2019], seg[seg.index >= 2023]):
        ax.plot(part.index, part.values, color=COL[g], lw=2, marker="o", ms=3.5)
    off = {"other": 1.6, "energy": -1.6}.get(g, 0)
    ax.text(2024.3, seg.iloc[-1] + off, LAB[g], color=INK, fontsize=7.5, va="center")
ax.axvline(2013.7, color=MUTED, lw=0.8, ls="--")
ax.text(2013.8, 46, "BRI announced\nSept 2013", fontsize=7, color=MUTED)
ax.axvspan(2019.5, 2022.5, color="#f2f1ed")
ax.text(2021, 2, "KZ product data\nsuppressed", fontsize=6.5, color=MUTED, ha="center")
ax.set_ylabel("China's share of Kazakhstan's exports, %")
ax.set_xlim(2004.5, 2028.5); ax.set_ylim(0, 50)
ax.set_title("China's share of Kazakhstan's exports, by product group (Kazakhstan-reported)", fontsize=9.5)
foot(fig)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(F / "fig_r2_china_share_by_group.png", dpi=200); plt.close(fig)

# Fig R3: event study (PPML), China x year x group, base 2013
es = pd.read_csv(T / "ppml_event_study.csv")
fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.9), sharey=True)
for ax, g in zip(axes, ["agrifood", "metals_ores", "energy"]):
    d = es[es["group"] == g].sort_values("year")
    for part in (d[d["year"] <= 2019], d[d["year"] >= 2023]):
        ax.plot(part["year"], part["b"], color=COL[g], lw=2, marker="o", ms=3.5)
        if g != "energy":
            ax.fill_between(part["year"], part["ci_lo"], part["ci_hi"], color=COL[g], alpha=0.15, lw=0)
    ax.axhline(0, color=INK, lw=0.7); ax.axvline(2013, color=MUTED, lw=0.7, ls="--")
    ax.set_title(LAB[g] + ("\n(one chapter: no CI)" if g == "energy" else "\n(95% CI, clustered by HS-2)"),
                 fontsize=8)
    ax.set_xticks([2005, 2013, 2019, 2024])
axes[0].set_ylabel("log China/RoW ratio vs 2013")
foot(fig, "PPML with product-year and product-destination fixed effects (Script 62).")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(F / "fig_r3_event_study.png", dpi=200); plt.close(fig)

# Fig R4: bilateral balance decomposition 2013 -> 2024 (China-reported)
dec = pd.read_csv(T / "trade_balance_decomposition.csv")
r = dec[(dec["from"] == 2013) & (dec["to"] == 2024)].iloc[0]
items = [("Energy exports", r["d_exports_energy_bn"], COL["energy"]),
         ("Metals and ores exports", r["d_exports_metals_ores_bn"], COL["metals_ores"]),
         ("Agri-food exports", r["d_exports_agrifood_bn"], COL["agrifood"]),
         ("Other exports", r["d_exports_other_bn"], COL["other"]),
         ("Imports from China (minus)", -r["d_imports_total_bn"], "#6250d6")]
fig, ax = plt.subplots(figsize=(7.2, 3.2))
y = np.arange(len(items))[::-1]
for yi, (lab, v, col) in zip(y, items):
    ax.barh(yi, v, color=col, height=0.55)
    ax.text(v + (0.2 if v >= 0 else -0.2), yi, f"{v:+.1f}", va="center", ha="left" if v >= 0 else "right",
            fontsize=8, color=INK)
ax.set_yticks(y); ax.set_yticklabels([i[0] for i in items])
ax.axvline(0, color=INK, lw=0.8); ax.set_xlim(-18, 8)
ax.set_xlabel("Contribution to the change in Kazakhstan's balance with China, USD bn")
ax.set_title(f"Balance {r['balance_from_bn']:+.1f} bn (2013) to {r['balance_to_bn']:+.1f} bn (2024), "
             f"China-reported data", fontsize=9.5)
foot(fig)
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(F / "fig_r4_balance_decomposition.png", dpi=200); plt.close(fig)

# Fig R5: Chinese official finance commitments to Kazakhstan (AidData GCDF 3.0)
a = pd.read_csv(T / "aiddata_by_year.csv").set_index("Commitment Year").iloc[:, 0]
fig, ax = plt.subplots(figsize=(7.2, 3.0))
ax.bar(a.index, a.values, color="#2a78d6", width=0.75)
ax.axvline(2013.5, color=MUTED, lw=0.8, ls="--")
ax.text(2013.7, 11.5, "BRI announced", fontsize=7, color=MUTED)
ax.set_ylabel("USD bn, constant 2021")
ax.set_title("Chinese official finance commitments to Kazakhstan by year, 2000-2021", fontsize=9.5)
fig.text(0.01, 0.005, "Source: AidData GCDF 3.0, projects recommended for aggregates (n = 155); author's calculations.",
         fontsize=6.5, color=MUTED)
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(F / "fig_r5_aiddata_by_year.png", dpi=200); plt.close(fig)

# Fig R6: diversification, number of HS-2 chapters above USD 1m, China vs RoW
dv = pd.read_csv(T / "diversification_indices.csv")
fig, ax = plt.subplots(figsize=(7.2, 3.0))
for ser, col in [("KZ-reported exports to China", "#2a78d6"), ("KZ-reported exports to rest of world", "#eb6834")]:
    d = dv[dv["series"] == ser].set_index("year")["HHI"]
    for part in (d[d.index <= 2019], d[d.index >= 2023]):
        ax.plot(part.index, part.values, color=col, lw=2, marker="o", ms=3.5)
    ax.text(2024.3, d.iloc[-1], ser.replace("KZ-reported exports to ", "to "), fontsize=7.5, va="center")
ax.axvline(2013.7, color=MUTED, lw=0.8, ls="--")
ax.set_xlim(2004.5, 2027.5); ax.set_ylim(0, 0.7)
ax.set_ylabel("Herfindahl index (HS-2)")
ax.set_title("Concentration of Kazakhstan's export basket: China vs rest of world", fontsize=9.5)
foot(fig, "2020-2022 excluded.")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(F / "fig_r6_hhi.png", dpi=200); plt.close(fig)
print("figures written")

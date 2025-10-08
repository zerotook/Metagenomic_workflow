library(readr)
library(dplyr)
library(pheatmap)
library(RColorBrewer)

# Read your full phylum-level abundance table
phyla <- read_csv("D:/Research/Project_CAFO ARG/Metagenomic Analysis/Bacterial Community/Pavian/Phylum_clade.csv")

# Remove unnecessary columns and ensure names are unique
abund_all <- phyla %>%
  select(-lineage) %>%
  mutate(name = make.unique(as.character(name)))

# Convert to matrix
mat <- abund_all %>%
  select(-name) %>%
  as.matrix()

rownames(mat) <- abund_all$name

# Apply log10(x + 1) transformation
mat_log <- log10(mat)

# Define color palette
my_colors <- colorRampPalette(c("white", "pink", "red"))(100)

# Draw heatmap for all phyla
pheatmap(
  mat_log,
  cluster_rows = TRUE,
  cluster_cols = FALSE,
  show_rownames = TRUE,
  show_colnames = TRUE,
  fontsize_row = 10,
  fontsize_col = 9,
  main = "All Phyla (log10 abundance + 1)",
  color = my_colors
)

# Optional: save a large version if too big for RStudio viewer
# pheatmap(
#   mat_log,
#   cluster_rows = TRUE,
#   cluster_cols = FALSE,
#   show_rownames = TRUE,
#   show_colnames = TRUE,
#   fontsize_row = 10,
#   fontsize_col = 9,
#   filename = "All_Phyla_heatmap.png",
#   width = 9,
#   height = 12,
#   color = my_colors
# )

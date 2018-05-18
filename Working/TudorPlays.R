#
# Paul Evans (pevans@sandiego.edu)
# 27 April 2018
#
library(stylo)
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist_init.txt",
  mfw.min = 65, mfw.max = 65,
  mfw.list.cutoff = 300,
  write.jpg.file = TRUE,
  custom.graph.title = "Initial List",
  custom.graph.filename = "Initial_CA_65_MFWs_Culled_0"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist_cait.txt",
  mfw.min = 65, mfw.max = 65,
  mfw.list.cutoff = 300,
  write.jpg.file = TRUE,
  custom.graph.title = "Cait's List",
  custom.graph.filename = "Cait_CA_65_MFWs_Culled_0"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)


#
# Paul Evans (pevans@sandiego.edu)
# 23 March 2016
#
setwd("~/Work/GentylnesAndNobylyte")
library(stylo)
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist0.txt",
  mfw.list.cutoff = 250,
  write.jpg.file = TRUE,
  custom.graph.filename = "G_and_N_CA_100_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
##
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist1.txt",
  mfw.min = 65, mfw.max = 65,
  mfw.list.cutoff = 250,
  write.jpg.file = TRUE,
  custom.graph.filename = "G_and_N_CA_65_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)

#
# Paul Evans (pevans@sandiego.edu)
# 27 April 2018
#
setwd("~/Work/GentylnesAndNobylyte/Working")
library(stylo)
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist_cait.txt",
  mfw.list.cutoff = 300
)
summary(stylo.results)
print(stylo.results$features.actually.used)


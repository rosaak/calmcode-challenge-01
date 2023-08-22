library(tidyverse)
df <- read.table("message.csv", sep = ",", header = 1)
# head(df)
qplot(data = df, x = x, y = y, geom = "point", color = "red")

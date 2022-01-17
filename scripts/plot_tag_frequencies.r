library(ggplot2)

dat <- read.csv("../data/tag_frequencies.csv", sep=" ")
dat$id <- row.names(dat)
dat$id = as.numeric(as.character(dat$id))
print(dat)

p <- ggplot(dat, aes(x=id, y=count)) +
     geom_point(size=4, shape="+") +
     xlab("Tag ID") +
     ylab("Tag Frequency") +
     scale_x_log10() +
     scale_y_log10() +
     theme_bw()

ggsave("plots/tag_frequencies.pdf", p, width=4, height=3)

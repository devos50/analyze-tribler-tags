library(ggplot2)

dat <- read.csv("../data/torrent_to_tag_frequencies.csv")
dat$id <- row.names(dat)
dat$id = as.numeric(as.character(dat$id))
print(dat)

p <- ggplot(dat, aes(x=id, y=tag_count)) +
     geom_point(size=4, shape="+") +
     xlab("Torrent ID") +
     ylab("Tags Received") +
     scale_x_log10() +
     scale_y_log10() +
     theme_bw()

ggsave("plots/torrent_to_tag_frequencies.pdf", p, width=4, height=3)

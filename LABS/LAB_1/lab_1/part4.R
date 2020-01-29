#import the sample dataset before running
p <- ggplot(sample, aes(winner, error))
p + geom_point(aes(shape=factor(victory),size=total,colour=factor(victory)))+ geom_text_repel(aes(colour=factor(year),label=player), position = position_jitter(width=5, height=1.5) ) + facet_wrap(~year) + geom_line(aes(colour=factor(year)))
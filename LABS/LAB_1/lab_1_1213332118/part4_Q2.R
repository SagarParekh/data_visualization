#import the big3 dataset before running
p <- ggplot(sample, aes(return,break.))

p + geom_point(aes(shape=factor(victory),size=total,color=ifelse((victory==0),"lose","win")))+ geom_text_repel(aes(label=player, color=ifelse((victory==0),"lose","win")), position = position_jitter(width=5, height=1.5),vjust=1.8) + facet_wrap(~year) + scale_shape_manual(labels = c("Lose", "Win"),values=c(13,21)) + labs(title = "Tennis Finals\n", color = "Color\n", shape="Shape\n") + geom_line()

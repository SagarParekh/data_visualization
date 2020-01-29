#import dataset big3.csv
#only look at the big 3 players
p <- ggplot(big3, aes(factor(year), winner1))
p + geom_boxplot() + facet_grid(~player1)+ geom_jitter(height = 0)

# distribution and density
p + geom_violin() +facet_grid(~player1)+ geom_jitter(height = 0)

# regression line
ggplot(big3, aes(x=total1, y=winner1, size=total1, color=player1)) + geom_point()+geom_smooth(method=lm, se=F)

# regression + prediction
ggplot(big3, aes(x=total1, y=winner1, size=total1, color=player1)) + geom_point()+ geom_smooth(method=lm)

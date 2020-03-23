library(maps)
map('county', 'arizona', fill = TRUE, col = palette())
all_county_data <- map_data("county")
az_county_data <- sqldf("select * from all_county_data where region = 'arizona'")


library(maptools)
library(rgdal)
#states.shp <- readShapeSpatial("./2012election/elpo12p010g.shp")
states.shp <- st_read("D:/sem 6/DV/LABS/Lab_4_maps/map_zip/map_zip/2012election/elpo12p010g.shp")
#states.shp <- readOGR("./2012election","elpo12p010g.shp")
head(states.shp)


#getting state boarder info #i.e.fortify(shape, region = "NAME")
states.shp.f <- fortify(states.shp, region = "STATE_FIPS")
gphead(states.shp.f)

#change states.shp.f$id to STATE_FIPS
colnames(states.shp.f)[6] <- "STATE_FIPS"

#sample some data
mydata <- data.frame(states.shp.f)
mydata1 <- sqldf("select * from mydata where STATE_FIPS = '04'")


#merge with coefficients and reorder
merge.shp.coef<-merge(mydata1, states.shp, by="STATE_FIPS", all.x=TRUE)

final_plot<-merge.shp.coef[order(merge.shp.coef$order), ] 




setwd("~/ABhack/ABInvHack")
beer = read.csv("mercuryc.csv", header=TRUE, sep=",")
b_time = beer$time
hours = beer$hour
time_id = beer$id

b_volume = beer$volume
oz_to_liter = 0.354882
glass_per_serve = round(b_volume/oz_to_liter)
plot(time_id, glass_per_serve, type="n")
lines(time_id, glass_per_serve)

t_volume = sum(b_volume)
total_glass_count = sum(glass_per_serve)

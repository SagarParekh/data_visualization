library(shiny)
shinyUI (
  pageWithSidebar
  (
    #Specify Application title
    headerPanel ("Differences Between Champions and Runnerups"),
    #Sidebar with controls to select the variable to plot against match result
    sidebarPanel
    ( selectInput ("variable", "Variable:", list("Winner" = "winner",
                                                 "Error" = "error",
                                                 "Total" = "total")
    ),
      # Add an optional input: to specify whether outliers should be displayed
      checkboxInput ("outliers", "Show outliers", FALSE)
    ),
    #Show the caption and plot of the requested variable against match result as outputs
    mainPanel (h3(textOutput("caption")),
      plotOutput("tennisPlot")
    ) #
  ) # pageWithSidebar end
) #UI end

library(shiny)
#library(datasets)
#library(foreign)

#tennis <-read.csv("USOP.csv") # Why do we put data here instead of in the ui.R file?

# Define server logic required to plot various variables against match result
shinyServer(function(input, output) 
{   
  # Construct the formula for the title of the plot 	
  formulaText <- reactive(
    {	paste(input$variable, "against match results") }
    )
  
  # Return the formula text for printing as a caption
    output$caption <- renderText (
                  {	 formulaText() }
                )

  # Generate a boxplot of requested variable against result and include outliers if requested
    output$tennisPlot <- renderPlot(
                {	#Construct a formula for the plot
                  boxplot(as.formula(paste(input$variable, "~victory" )), 
                          data = sample,
                          outline = input$outliers,
                          col="orange")
                }
    )
}		
)

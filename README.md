# Final Project Overview and reflection

## Project Name

StockInfo

## Team Members
- Curtis O'Keeffe

## 1. Project Overview
My Web application, **StockInfo**, is a stock information site that allows users to view key information about stocks of their choice. Features include dynamic charts with various time ranges, current price display, and market cap information, all accessible through an easy-to-navigate interface.

### Target Audience
Individuals who need quick access to basic stock metrics without the hassle of account sign-ups or ad interruptions.

### Standout Aspect
Focuses on essential information, offering a simpler alternative to information-heavy sites.

## 2. Usage Guidelines
To use **StockInfo**, run it locally as it is not yet deployed. Users can browse featured stocks or search for any publicly listed stock using its symbol.

### Usage Steps
- Enter the stock symbol (e.g., "MSFT" or "msft", but not "Microsoft")
- Note: The API allows a maximum of 25 requests per day.

## 3. Dependencies
- **Flask**: A micro web framework for building web applications.
- **DateTime**: For manipulating dates and times.
- **Alpha Vantage API**: For fetching financial market data.
- **JSON**: Built-in module for handling JSON data.
- **Pandas**: For data manipulation and analysis.
- **Bootstrap**: For creating the navigation bar.
- **config**: For storing API keys.

## 4. Project Structure
The structure of **StockInfo** is outlined as follows:
- `FinalProject`
    - `Main`
        - `app.py` (Main programming file)
        - `config.py` (API key storage)
        - `requirements.txt` (Deployment dependencies, not used)
        - `__init__.py` (Deployment purposes, not used)
        - `.gitignore` (Standard)
        - `README.md` (Project information)
        - `__pycache__` (Fast access data storage)
        - `Templates` (HTML files)
            - `index.html` (Homepage)
            - `search_result.html` (Search result page)
            - `error.html` (error page)
            - `mercadolibre.html` (Mercado Libre stock page)
            - `amazon.html` (Amazon stock page)
            - `nvidia.html` (Nvidia stock page)
            - `microsoft.html` (Microsoft stock page)
            - `drhorton.html` (DrHorton stock page)
  

## 5. Collaboration Information
No collaboration.

## 6. Acknowledgments
- **Alpha Vantage API**: For stock information.
- **Bootstrap**: For navigation bar design.
- **Pandas**: For data manipulation.
- **Datetime**: For date handling.
- **ChatGPT**: For debugging assistance.
- **GitHub Copilot**: For code writing and debugging.
- **GitHub**: For information and repository hosting.

## 7. Reflection
### Process Point of View
I found that the process of developing this project was successful for the most past, as i met and exceeded my initial expectation in terms of final functionality and presentation of the site. The process of fetching the Alpha Vantage API information, converting it into a usable format and presenting it on a chart was easier then expected, but it was far from complete. 

initially, the data was presented backwards, from newest to oldest left to right, which caused the current price to be the oldest datapoint for the selected time period. this was an issue as it gave inaccurate data and the graph was presented incorrectly. once this was fixed, i noticed issues with the quantity of data. there was a fixed amount of data that was being used for all the date ranges, which cuased the 1 year range to show far more info then the 1 day range, which may have only had 1 or 2 data points. to fix this, i used interday information, to fetch the stock price at smaller intervals such as every 5 minutes or 120 minutes. This fixed the presentation of the information and was a constantc challenge i was working on.

Another main challenge was the API useage cap that i would keep running into. this was 25 requests a day and made it hard for me to work on the project for more then one hour. i tried to fix this by importing the API data into a static file, but once i started fetching data at 5 min intervals, this became unrealistic and my testing had decreased so i was not hitting my limit.

For the formatting and presentation of the site, i wanted to make something simple yet professional. i did not want my site to look like something built by someone with no UI design knowledge so i utilised ChatGPT to create an outline for a professional looking simple theme, using a transparent blue background across the site, with text formated correctly and the navigaion bar adding the functionallity of the typical web application. 

For testing the project, i would log data at different stages through out the process, to identify where issues occured. for example, i would log the quantity of data when it was fetched, transformed and passed to different routes and edited for the different ranges. this allowed me to see if the data quantity issue was due to fetching, manipulating or passing allowing me to fix it. This allowed me to catch errors that even ChatGPT and Copilot were unable to identify.

Additionally, i designated my DrHorton.html page to show the native error message rather then redirecting to error.html. which is where i would want the user to be sent, so i could better identify the error that was occuring as my error page shows a general message, and often the error was just maximum API requests rather then an actual issue in my code. Looking forward, i would have created a seperate html page just for this rather then using DrHorton as this casued some issues that ony DrHortons page would show, rather then an unused testing page.

I was happy with the functionality as i initially decided to only preset 5 stocks as well as have a fixed time range however once i reached this goal with plenty of time to spare, i started adding additional features such as the time range feature and the search feature as i felt this made the site a lot more practical and useful.

The main change i would make if i were to continue working on this project would to deploy it so it can be used by everyone. i tried this early on, but struggled to get it to run and figured i would continue working on the functionallity before deploying. 


### Learning Perspective

Through the completion of this project, i was able to integrate my existing computer science knowledge to building a web application, which is the area in computer science that i have had the least experience with. I found that as soon as i understood the structure of the project, and the how flask worked, i was really able to utilise my existing knowledge to quickly build a functional site. This made it alot easier for me, and allowed me to relise how easy it is to learn new programming concpets and uses if you have an existing foundational knowledge.

ChatGPT assisted greatly in the inital structuring and set up of my project, as i gave it a run down on my idea and asked it to create a setp by step guide that i could use to get my project started, as i was a bit unsure where to start. I also used it to diagnose errors, as it was much quicker then me looking through the lines of code i suspected was the issue. this was not always reliable and i found that i was having to use my own knowledge at least partially most of the time. I also used Github Copilot, which was extremely useful at predicting what i would type, allowing me to just have to strat each line. i would also use it to make changes on multiple routes so i would not have to do each route by hand. for example, i would give it amazons route and tell it to change all the other stocks routes to adapt the same functionallity. 

Looking forward, i am keen to use the skills i have learnt whenever possible. this may be in the form of a personal project, or in internships as i am looking more in the tech field. Additionally, this project allowed me to give an example of my programming skills, which is beneficial for future employment oportunities. Furthermore, having an understanding of these concepts allows us to understand how the internet works as a whole, and how the sites we use and interact with everyday came to be.

If i were to start this project again, i would have planned to add more features at the start, rather then integrating them alnog the way. this would allow me to build the foundation around these features so i dont need to change as much later on.

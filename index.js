import axios from 'axios';
import * as cheerio from 'cheerio';

// Fetch and scrape the web page
async function scrapePage() {
    try {
        const response = await axios.get('https://quotes.toscrape.com/');

        // Load the HTML into cheerio
        const $ = cheerio.load(response.data);

        // Extract quotes and authors
        const quotesData = $('.quote').map((i, el) => {
            const quote = $(el).find('.text').text();
            const author = $(el).find('.author').text();

            // Return an object with both quote and author
            return {
                quote,
                author
            };
        }).get(); // Convert cheerio object to an array

        // Return quotes and authors inside the cheerio object
        const cheerioObject = {
            quotesData
        };

        console.log(cheerioObject);
    } catch (error) {
        console.error('Error fetching the page:', error);
    }
}

scrapePage();

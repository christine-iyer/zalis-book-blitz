import axios from 'axios';
import * as cheerio from 'cheerio';

// Fetch and scrape the web page
async function scrapePage() {
    try {
        const response = await axios.get('https://quotes.toscrape.com/');

        // Load the HTML into cheerio
        const $ = cheerio.load(response.data);

        // Extract data using Cheerio (like jQuery)
        let quotes = $('.text').map((i, el) => $(el).text()).get(); // Fixed selector for text
        let authors = $('.author').map((i, el) => $(el).text()).get(); // Fixed selector for authors

        console.log('Quotes:', quotes);
        console.log('Authors:', authors);
    } catch (error) {
        console.error('Error fetching the page:', error);
    }
}

scrapePage();

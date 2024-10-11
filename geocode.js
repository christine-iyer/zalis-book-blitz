// function geocodeAddresses() {
//      var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Sheet1"); // Change the sheet name if needed
//      var dataRange = sheet.getRange(2, 2, sheet.getLastRow() - 1, 2); // Get columns B and C
//      var data = dataRange.getValues();
     
//      // Define the fixed part of the address
//      var town = "Cape Elizabeth, ME 04107";
     
//      // OpenCage API key
//      var apiKey = '5_e-zwzZL93BpIKHQNnSPNeEwJz269UvVkpTEth1sDI'; // Replace with your OpenCage API key
   
//      for (var i = 0; i < data.length; i++) {
//        var streetAddress = data[i][0]; // Column B (Street address)
//        var unit = data[i][1];          // Column C (Unit number)
       
//        // Combine street address and town to form the full address
//        var fullAddress = streetAddress + " " + unit + ", " + town;
   
//        // Get the latitude and longitude via the OpenCage API
//        var geocodeResult = geocodeWithOpenCage(fullAddress, apiKey);
       
//        if (geocodeResult) {
//          // Write latitude and longitude into columns D and E
//          sheet.getRange(i + 2, 4).setValue(geocodeResult.lat); // Column D for Latitude
//          sheet.getRange(i + 2, 5).setValue(geocodeResult.lng); // Column E for Longitude
//        } else {
//          // If geocoding fails, mark the cell as "Not found"
//          sheet.getRange(i + 2, 4).setValue("Not found");
//          sheet.getRange(i + 2, 5).setValue("Not found");
//        }
//      }
//    }
   
//    // Helper function to call the OpenCage API
//    function geocodeWithOpenCage(address, apiKey) {
//      var url = 'https://api.opencagedata.com/geocode/v1/json?q=' + encodeURIComponent(address) + '&key=' + apiKey;
     
//      // Call the OpenCage API
//      var response = UrlFetchApp.fetch(url);
//      var json = JSON.parse(response.getContentText());
   
//      // Check if a valid result is returned
//      if (json.results && json.results.length > 0) {
//        var location = json.results[0].geometry;
//        return { lat: location.lat, lng: location.lng };
//      } else {
//        return null;
//      }
//    }
   // Helper function to call the Nominatim API
function geocodeWithNominatim(address) {
     var url = 'https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(address);
     
     try {
       // Call the Nominatim API
       var response = UrlFetchApp.fetch(url);
       var json = JSON.parse(response.getContentText());
       
       // Log the full API response for debugging
       Logger.log(json);
       
       // Check if a valid result is returned
       if (json && json.length > 0) {
         var location = json[0];
         Logger.log("Lat: " + location.lat + ", Lng: " + location.lon);
         return { lat: location.lat, lng: location.lon };
       } else {
         Logger.log("No results found for: " + address);
         return null;
       }
     } catch (error) {
       Logger.log("Error during Nominatim API request: " + error);
       return null;
     }
   }
   
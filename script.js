// This function will simulate an exchange rate conversion
// In real-world apps, you would fetch this data from an API

const exchangeRates = {
    USD_EUR: 0.91,  // Example: 1 USD = 0.91 EUR
    EUR_USD: 1.10   // Example: 1 EUR = 1.10 USD
};

// Function to perform currency conversion
function convertCurrency() {
    // Get input values
    const amount = parseFloat(document.getElementById('amount').value);
    const fromCurrency = document.getElementById('from-currency').value;
    const toCurrency = document.getElementById('to-currency').value;

    // If the amount is invalid, show an error
    if (isNaN(amount) || amount <= 0) {
        document.getElementById('result').textContent = "Please enter a valid amount.";
        return;
    }

    // Check conversion logic based on selected currencies
    let convertedAmount;
    if (fromCurrency === 'USD' && toCurrency === 'EUR') {
        convertedAmount = amount * exchangeRates.USD_EUR;
    } else if (fromCurrency === 'EUR' && toCurrency === 'USD') {
        convertedAmount = amount * exchangeRates.EUR_USD;
    } else {
        // If both currencies are the same
        convertedAmount = amount;
    }

    // Display the result
    document.getElementById('result').textContent = `Converted amount: ${convertedAmount.toFixed(2)} ${toCurrency}`;
}

// Event listener for the convert button
document.getElementById('convert-button').addEventListener('click', convertCurrency);

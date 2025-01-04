import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

# Streamlit UI
st.title("Stock Price Forecasting Dashboard")

# User Input for Stock Ticker
ticker = st.text_input("Enter Stock Ticker", "AAPL")
start_date = st.date_input("Start Date", value=pd.to_datetime("2015-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-12-31"))

# Fetch Data
if st.button("Fetch Data"):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        st.subheader(f"Historical Data for {ticker}")
        st.write(data.tail())

        # Plot Historical Data
        st.subheader("Historical Closing Prices")
        st.line_chart(data["Close"])

        # Train ARIMA Model
        st.subheader("Training ARIMA Model")
        train_data = data["Close"].dropna()
        model = ARIMA(train_data, order=(5, 1, 0))  # ARIMA(p, d, q)
        model_fit = model.fit()
        st.write("ARIMA Model Summary:")
        st.text(model_fit.summary())

        # Forecast
        forecast_steps = 30
        forecast = model_fit.forecast(steps=forecast_steps)
        forecast_dates = pd.date_range(
            data.index[-1], periods=forecast_steps + 1, freq="B"
        )[1:]

        # Plot Forecast
        st.subheader("Stock Price Forecast")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(data.index, data["Close"], label="Actual Prices")
        ax.plot(forecast_dates, forecast, label="Forecasted Prices", linestyle="--")
        ax.legend()
        ax.set_title(f"{ticker} Price Forecast")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")

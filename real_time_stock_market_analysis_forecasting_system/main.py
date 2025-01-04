{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/titiksha/dev/cla_christmas_break/.venv/bin/python'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import sys\n",
    "sys.executable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[*********************100%***********************]  1 of 1 completed\n"
     ]
    }
   ],
   "source": [
    "# download historical stock data \n",
    "ticker = \"AAPL\"\n",
    "data = yf.download(ticker, start=\"2015-01-01\", end=\"2024-12-31\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th>Price</th>\n",
       "      <th>Close</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ticker</th>\n",
       "      <th>AAPL</th>\n",
       "      <th>AAPL</th>\n",
       "      <th>AAPL</th>\n",
       "      <th>AAPL</th>\n",
       "      <th>AAPL</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2015-01-02</th>\n",
       "      <td>24.347170</td>\n",
       "      <td>24.817055</td>\n",
       "      <td>23.906234</td>\n",
       "      <td>24.805920</td>\n",
       "      <td>212818400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-05</th>\n",
       "      <td>23.661270</td>\n",
       "      <td>24.195737</td>\n",
       "      <td>23.474208</td>\n",
       "      <td>24.115567</td>\n",
       "      <td>257142000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-06</th>\n",
       "      <td>23.663500</td>\n",
       "      <td>23.924052</td>\n",
       "      <td>23.300507</td>\n",
       "      <td>23.725854</td>\n",
       "      <td>263188400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-07</th>\n",
       "      <td>23.995312</td>\n",
       "      <td>24.095523</td>\n",
       "      <td>23.761482</td>\n",
       "      <td>23.872829</td>\n",
       "      <td>160423600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-01-08</th>\n",
       "      <td>24.917271</td>\n",
       "      <td>24.975172</td>\n",
       "      <td>24.206875</td>\n",
       "      <td>24.324905</td>\n",
       "      <td>237458000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Price           Close       High        Low       Open     Volume\n",
       "Ticker           AAPL       AAPL       AAPL       AAPL       AAPL\n",
       "Date                                                             \n",
       "2015-01-02  24.347170  24.817055  23.906234  24.805920  212818400\n",
       "2015-01-05  23.661270  24.195737  23.474208  24.115567  257142000\n",
       "2015-01-06  23.663500  23.924052  23.300507  23.725854  263188400\n",
       "2015-01-07  23.995312  24.095523  23.761482  23.872829  160423600\n",
       "2015-01-08  24.917271  24.975172  24.206875  24.324905  237458000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe thead tr:last-of-type th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr>\n",
       "      <th>Price</th>\n",
       "      <th>Close</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ticker</th>\n",
       "      <th>AAPL</th>\n",
       "      <th>AAPL</th>\n",
       "      <th>AAPL</th>\n",
       "      <th>AAPL</th>\n",
       "      <th>AAPL</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2024-12-23</th>\n",
       "      <td>255.270004</td>\n",
       "      <td>255.649994</td>\n",
       "      <td>253.449997</td>\n",
       "      <td>254.770004</td>\n",
       "      <td>40858800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2024-12-24</th>\n",
       "      <td>258.200012</td>\n",
       "      <td>258.209991</td>\n",
       "      <td>255.289993</td>\n",
       "      <td>255.490005</td>\n",
       "      <td>23234700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2024-12-26</th>\n",
       "      <td>259.019989</td>\n",
       "      <td>260.100006</td>\n",
       "      <td>257.630005</td>\n",
       "      <td>258.190002</td>\n",
       "      <td>27237100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2024-12-27</th>\n",
       "      <td>255.589996</td>\n",
       "      <td>258.700012</td>\n",
       "      <td>253.059998</td>\n",
       "      <td>257.829987</td>\n",
       "      <td>42355300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2024-12-30</th>\n",
       "      <td>252.199997</td>\n",
       "      <td>253.500000</td>\n",
       "      <td>250.750000</td>\n",
       "      <td>252.229996</td>\n",
       "      <td>35557500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Price            Close        High         Low        Open    Volume\n",
       "Ticker            AAPL        AAPL        AAPL        AAPL      AAPL\n",
       "Date                                                                \n",
       "2024-12-23  255.270004  255.649994  253.449997  254.770004  40858800\n",
       "2024-12-24  258.200012  258.209991  255.289993  255.490005  23234700\n",
       "2024-12-26  259.019989  260.100006  257.630005  258.190002  27237100\n",
       "2024-12-27  255.589996  258.700012  253.059998  257.829987  42355300\n",
       "2024-12-30  252.199997  253.500000  250.750000  252.229996  35557500"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1IAAAH9CAYAAAAQ800VAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAkVxJREFUeJzt3Qd8U2X3wPFD96CDsvfeS0BABFEBRcGB4kIcKK/rdevrfN0L9XXvv3sr7i2CgIqyUfbemzI76c7/c572pjdp0kXbpMnv+/nE3Htzm948piWn53nOqeNwOBwCAAAAACi3kPKfCgAAAABQBFIAAAAAUEEEUgAAAABQQQRSAAAAAFBBBFIAAAAAUEEEUgAAAABQQQRSAAAAAFBBBFIAAAAAUEEEUgAAAABQQQRSAABUwrvvvit16tSRhQsX+uT7P/DAA+b7AwB8g0AKAILQK6+8Yj6EDxw4sFzn33777eb8888/3+PjmzdvNo9bt9DQUGnVqpWcddZZsnjxYpdz9fHrrruuUtf9559/yqmnnirNmzeXqKgo8z1OP/10+fjjj53nZGZmmiDjt99+E3+l12Yfr/DwcGnXrp1ccsklsnHjRl9fHgCgHAikACAIffTRR9KmTRuZP3++rF+/vtRzHQ6HfPLJJ+b877//XtLS0ryeO27cOPnggw/k7bfflgsvvFBmzJghxxxzTIlgqjI+//xzGTp0qOzZs0duvPFGefHFF+Wiiy6SgwcPyhtvvOESSD344IN+HUhZbrjhBjNer7/+uowePVomT54s/fv3l507d5b5tffcc48cPny4Rq4TAFBSmIdjAIAAtmnTJpk9e7Z89dVXctVVV5mg6v777/d6vgYk27dvN0HRyJEjzdddeumlHs/t27evCW4sgwcPljPOOENeffVV+b//+78jum7NMnXr1k3mzp0rERERLo8lJydLbXTcccfJOeecY7Yvu+wy6dSpkwmu3nvvPbnrrrs8fk1GRobExsZKWFiYuQEAfIOMFAAEGQ2c6tWrZzIg+iFe98s6XwOYE088UUaMGFHm+XbDhg1zBm9HasOGDSZb4x5EqUaNGjmnGDZs2NBsa1bKmjqnQZhFA0INYDQYSUxMlDPPPFNWrVpV4jl37NghEydOlGbNmklkZKS0bdtWrrnmGsnJyfF6jZodGzBggLRo0ULWrFlT4dfoPl7WOqiVK1eaDJ/+fxsyZIjLY+4+/PBDcw0xMTHmfM3iTZ061eWcn3/+2TkGcXFx5r2wYsUKl3N2795tgjt9Lfr6mzZtasZKxxgAQEYKAIKOBkJnn322CUh0Kp5mixYsWGCCFHfZ2dny5Zdfyq233mr29Xz9cK0fsps0aVKu4EfVr1//iK+7devWMn36dJMd0w/3nmgQpa9HAx5dn6WvU/Xq1cvc//rrr2aNla5H0kBEp8bpFEHNnP39999m+qLSqXUajBw6dEiuvPJK6dKliwmsvvjiCzN10FMwt2/fPjnppJPkwIED8vvvv0v79u0r/Bq9jde5554rHTt2lMcee8xMtfRGg0d9Xccee6w89NBD5jrnzZtngseTTz7ZnKNTCTWjqNnFJ554wrweHTMN0P755x/nGIwdO9YEV9dff705plm/adOmydatW53nAEBQcwAAgsbChQv1U7hj2rRpZr+goMDRokULx4033ujx/C+++MKcv27dOrOfmprqiIqKcjz77LMu523atMmc9+CDDzr27t3r2L17t+O3335z9OnTxxz/8ssvnefq/rXXXlvha3/rrbfM10ZERDhOPPFEx7333uuYNWuWIz8/3+U8/f563v3331/iOY466ihHo0aNHPv373ceW7JkiSMkJMRxySWXOI/pth5bsGBBiefQMVPvvPOO+T56zq5duxzdu3d3tGvXzrF58+YyX8vMmTPN17799tvmenfu3On48ccfHW3atHHUqVPH+X31Neh548aNK/Ec1mMW/X+k13zWWWeVGBPrmtPS0hyJiYmOK664wuVx/f+VkJDgPH7w4EHz3P/73//KfC0AEKyY2gcAQZaNaty4sZmmp6xKfJ9++qnk5+d7PP/oo4+WDh06mH1rGpi36X261kqzQpqtOuGEE0yGRbMeVmboSFx++eUyZcoU87xave/hhx8209M0U6Nrvsqya9cuU/RiwoQJkpSU5Dyu2SrNJP30009mv6CgQL755htTDVBfuzv36XSaITv++OMlNzdX/vjjD5M5q8hr0vHS6YM6rrr+SddHuX/fq6++uszn0mvWa7/vvvskJCTE4zVrRkmzbJpZ1AyaddMqi1rBcebMmea86Ohok83S9XE6XREAUBJT+wAgSGigpAGTBlH2NUv6Afrpp5820+as6V9KP3BrcKGlyu2V/XQanE73W7t2rSmOYKfT4HQa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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "#plot closing price\n",
    "data['Close'].plot(figsize=(10,6),title=f\"{ticker} Stock Prices\", xlabel=\"Date\", ylabel=\"Price\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAnYAAAHWCAYAAAD6oMSKAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAA1ApJREFUeJzsnQV4U1cbx1/qrlCjBYq7uzOcbUyYu29MmcM3Yc7cx5i7DyYwYMPd3b1QKKW0pe7yPe9JTnJyc5PcJDfNzeX9PU+eaNN7cuX8z6uN6uvr64EgCIIgCILwefy8vQEEQRAEQRCEOpCwIwiCIAiC0Akk7AiCIAiCIHQCCTuCIAiCIAidQMKOIAiCIAhCJ5CwIwiCIAiC0Akk7AiCIAiCIHQCCTuCIAiCIAidEODtDdASdXV1kJWVBZGRkdCoUSNvbw5BEARBEARgL4ni4mJISUkBPz/7NjkSdgIo6tLS0ry9GQRBEARBEFZkZmZCamoq2IOEnQBa6vgPFxUV5e3NIQiCIAiCgKKiImZ44jrFHiTsBLj7FUUdCTuCIAiCILSEkjAxEnYEQRAEQRAa5ccNJ+Cr5XsVf56EHUEQBEEQhAYpr6qF//2xC+oqyxT/DZU7IQiCIAiC0GAmbIdnFzr9dyTsCIIgCIIgNMbJc+Uu/R0JO4IgCIIgCA1RXVsHQ15f5tLfkrAjCIIgCILQWMKEyKonRij+WxJ2BEEQBEEQGqGwvBqm/72HPU6ODoGMVy+E2PAgxX9Pwo4gCIIgCEIjbD1+zvT4z/sGOf33JOwIgiAIgiBcZH92ERSUVTn9d5+vOgqDXl0Kqw/lWrx+69eb2P11/ZpBYlSI099LdewIgiAIgiBcKEcy9t2VcPBMCYzqkAif39zb4d/8s/M0LN53Bvqmx8FL/+xjr93wxQZ44ZJOcNOAFrDrZKHps5OHtQJXIGFHEARBEAThJMsPnGWiDkGxJuVAdjH8tPEE3DuiFcSFBcG6o3lw349b2Xt/bDtl8Vl8fmmPpnDXd5vZ87Agf0iLCwNXIGFHEARBEAThJBuO5cu+XlpZw7pF/LU9iz1fdegs3DeiNTzy6w6b37XtRAF0fe4/0/MPr+sBrkIxdgRBEARBEE66YX/ZZFmS5M1/D7D795YcMok65MjZUisLHWfxI0NlXx/WNsHlbSOLHUEQBEEQhJNdIc6VVVu89uGyw7DrVCGcKaqw+vwqSYIEMrFbCrSID7d6ff20keDv1whchSx2BEEQBEEQTrD7lCHJoXPTKPj0xl6m11ccPAv7s4ttlip5fGw7uLp3GqBuu2toSwjw94M7h6Sb3t/7wlhIinY+E1aELHYEQRAEQRAKeG/xIfh4xWHomhrDnndOiYZBrRtbfS4xKhi6p8XAkkeHwci3VpheDw/yhxcv7QxPjGsH8RHB7LWnLuwIj45pByGB/qAGZLEjCIIgCIJwwL7TRfDO4oNQUV0HG42JE52aRkN4cAA8d3FHi89O6pnK7ls1iWCdI0Z3TISEyGAY1zkZggL8TKKOo5ao04ywmzFjBvTp0wciIyMhISEBLr30UjhwwBCEyKmoqID77rsP4uPjISIiAiZNmgRnzlimF584cQIuvPBCCAsLY9/z+OOPQ01NTQOPhiAIgiAIvfHndusEiLYJEez+lkHp8PZV3UyvD23bxOJz6K5dO/UCt92sPiPsVqxYwUTb+vXrYdGiRVBdXQ1jxoyB0tJS02cefvhhmDt3Lvz222/s81lZWXD55Zeb3q+trWWirqqqCtauXQvffPMNfP311/Dss896aVQEQRAEQeiFqJBAq9e6pRlcskhKTKjpcXpjy6SIRo0asXi6hqBRPebsaoyzZ88yixsKuKFDh0JhYSE0adIEfvzxR7jiiivYZ/bv3w8dOnSAdevWQf/+/WHBggVw0UUXMcGXmJjIPjNr1ix48skn2fcFBTluoFtUVATR0dHs/0VFRXl8nARBEARB+AavL9wPM5cfYY8bNQL48uY+MKK9uSzJudIq6PHiIvb42IwJTMyphTP6RBMWOym44UhcXBy737JlC7PijRo1yvSZ9u3bQ7NmzZiwQ/C+S5cuJlGHjB07lv0Ye/bsafAxEARBEAShH8qqatn9jf2bw/Znx1iIOiQ2PAiWPTaclStRU9T5fFZsXV0dTJkyBQYNGgSdO3dmr2VnZzOLW0yM2eSJoIjD9/hnRFHH3+fvyVFZWcluHBSBBEEQBEH4BodziuFAdgmM75wEfm7UflNCTnGFKeM1OtTaLSvngvUGmhN2GGu3e/duWL16dYMkbTz//PMe/z8EQRAEcT6TX1oFJ/LL4PctmTC+c7JsiRBXRN2ot1eanh96eTwEGuPYsEjw1uPnWDaqGrFtmzLyYf4ug5EoNEhz0km7rtj7778f5s2bB8uWLYPUVEOqMJKUlMSSIgoKCiw+j1mx+B7/jDRLlj/nn5Eybdo05vblt8zMTA+MiiAIgiDOP15dsB8e/mU7Kw3S88VFcOlHa+D79SfgoZ+3uS0Sq2vrLEQd0vbpBXDoTDFr93X3d1tg8g9b4eX5+9wuRPz2fwfgylmGsC/RcqdVNCE7cSc88MAD8Mcff8Dy5cshPd1chRnp1asXBAYGwpIlS1iZEwTLoWB5kwEDBrDneP/yyy9DTk4OS7xAMMMWgww7drSsL8MJDg5mN4IgCIIg1KO0sgZmrTAkGkj7pOaWVDGLWmJUCFTV1MHCPdkQGRIAI9o57o+K34mCUQ5MBf1s1VG4qncabM80GIK+WpMBJ/LK4Ilx7aFdUqRTY9h64hxcPnOt1esXd00BLROgFfcrZrz+9ddfrJYdj4nDDJDQ0FB2f/vtt8MjjzzCEipQrKEQRDGHGbEIlkdBAXfjjTfC66+/zr7j6aefZt9N4o0gCIIgGs5Y896SQ3Y/k5lfxoTdG//uh89WHWOvYeKBvRg1FGtyom7j/0bCjxtPwLuLD8HC3dlw5Ky5VBqyZH8Ou23430j2P5Xy4dLDFs+njm8P1/ZpBtFh8vF1WkETrtiPP/6YuUKHDx8OycnJptsvv/xi+sw777zDypmgxQ5LoKB7dc6cOab3/f39mRsX71Hw3XDDDXDTTTfBCy+84KVREQRBEMT5xf7sIkifNh8+XXnU4vUL2iewDgwdkw2lOkqNGaarDuWaPnPyXJnd70ZXLic4wCBffr17ACREhcDdQ1tBgF8jKKqogS3Hz8n+fb9XljCLX12d/SpvFdW1MG3OTli6P8f0WuuECLh7aEvNizrNWOyUlNILCQmBjz76iN1s0bx5c5g/f77KW0cQBEGcT5RX1bI6ZWq2eTofQNfltZ+ut3jtnau7QaeUaEiNNRTvDQ82/KZllTVMBO7PLjZ9tqCs2uJvd54sgNTYMIgLD4LTheWm16/r1wxeuayLxWdDg/yZ2KsxCkZboMWvsLwanhzX3uZn/tx2Cn7aaI65//HOftAtNcarJUx8zmJHEARBEN4UcihKMO7ri9XHoMOzC+HiD1ZDrQPLjkhBWRWz9Jyv7MkqZPFolTV1ptfeuKIrXNq9KbRNjIQwYyZpRLDhHhMbxr27yuI7HvhpG9z341YWnzdtzi6Y+OEalnSBv+3sLSdNn3t+YifZbbh9sDk+Py0uFObcOxC+uqUPbHtmNLQX4us+Xn6EJV/g/3hvsbXL+HBOienxh9f1gIGtGrN+sL6C72wpQRAEQXiA1xbuh6/XZli8diinBI7nlULLJoZeoCjy9mYVsQB8bOIugtakATOWssePjG4LD45sA+cLNbV1sP5oPjz863bTayjedj8/VvbzV/dJg2UHztr8vn92nmY3kfeXHIYv1xji8O4d3spU0kTKAyPbQGpcGIzqkMisfCJ/3z8Y1h/Ng5u+3Mieo6D7aeMJ9vjBka3h+/XH4cV/9sE3t/Zl1lrk2r5pcJHGEyV8pqWYt6CWYgRBEOcfLab+Y/M9DOjHSR8techNA5rDC5cYiudznvx9J/yy2ey6w1gyd8GpGWPKUMR8fVtfk6VLK2QVlMMVH6+FrELr0h9/3jcIugs9VKXjuvmrTbDyoFncoVjjrbocsfnpUdA4wvWEyGlzdpkEHWdw68aw+rAh1g+zc4srathjFOgo1LWAz7cUIwiCIIiGoLLGvvt0xJvLTaIO+XbdcfhZEAZosfprh2U5j32n3e9i9OWaDNhxshA2Hz8HL83bqygWvaFAlzPWiZOKunaJkUzU2hJ1CMapfXtbX7hvRCsmol68tDMrRfL0hR2sPjtS0rKrW1qMW6IOaSmTdctFHcJFHYIuYF+EhB1BEARx3oI11aSg6LDH1Dm7TI8zz5VDRbU5rgwZ/94qOHjGnBTgCi/O22t6/POmTPh3j3xrzIYCRQ5mky7YdRq6v/Af7Dpl6OnOCQ/yhzev7Kb4+x4f2x52PDuG9V1F7hjSkolCManhg+t6MGsep1+6oX+8O7RwouUXJkz4Itqy7RIEQRBEA/LLJrMLFeOyejaLhQcuaMNaXl332Qa77ttbB7WAAS3j2fMOyVGArUr3ZBmsdWPeWQmPj23H4vJeu6KrU67Ue77bYvXan9uyYGynJMB8Dn8P90SV8tf2U/DQz+YYOhGMZ/v85t4ufa9cb9c7h6TDsLZNWCwjjnNSr1STm/b+C1q79H9ERnVIgOcu7giNI4NZ/Bxm3l79yXoolyS+oMv90h5NwRehGDsBirEjCII4f1i89wzc8e1m9rhVk3BY8NBQCPRvZCprMf2v3fDNuuPs8ZA2jeH+Ea3hakk5D85lPZrCFb1S4frPrcXgw6PawkOjlCVULNx9Gu75fqvV6ygiUSTmlVbBgoeG2EwgUBtMGhn82lI4LRNL5yieTi2W7DsDSdEhrGyKJ5m7Iwue/Ws33D2sFdwzzL7VVsv6hCx2BEEQxHnHu4sPsk4FnO5psVbZrl2YK84g7I7nlUG/lvHMQrV4n2Vfcl5brU+LOFaKY/rfeyzeyy2pdCq4nzN78gDIzC+HKb9sZ62xxMSF5vHKXYquUlZVAx2f/dfq9eToEJZw8PJlXax+M08wskMiNAQXd0thN1+HYuwIgiAIXXAguxhWCNmW9hATIhC54P1Lupsn+a6pBmvRlb1TrT6H8WXcanXzwBasoK3Ipox8RdtUUlkD54xFerHYbq/mcXBR12Srz93+zWb2WWkdOWxY7woYO4cibt7OLMgvNcccYh05kXGdkqBnsxhY8fgIeOPKbg0i6gjnIYsdQRAE4fNgJiomLSBz7x8MXYxCTCpgMK4LC+CK2Y/YxSBWUvcMQXfnfw8PZTXuru/XjL02pmMis6RhEdsnZxusazFhQRau0f7phrg7DnZXwCLI2B3BFrhtA2YsMT1f8ugwdh8g43LF/419TLF3KVJVUwcXvr+aPcbtxYLASjlXWgU9Xlxket40JhRem9QVbvjC0qWMcWm3DDIXACa0C8ltgiAIwifB+K8fNhyH//Zkm0QdsuKguccnp6iiGvq+spglPXSabnYvvndNd1aI1hYoklD48fgujL9DS9rVfQxCDzlVYG53haB4xB6mQ9s2Mb32z67TsPZwLqv9JmdVXH4wx0JsYistDjavl4I9T9FCyR9zZszfx8aIt/t+sI7VkyLtq4pjkYq6/S+OI1HnQ5CwIwiCIDQPtoCa8vM2uPWrjazt1Pxdp1nHiKf+2A13SbJI3/zvIGw5nm9q9o7WvK7P/WdV2qRPi1i4pHtTl3uAYkIFt+JJ6ZseB1/f0sf0/LHfdsB1n29gdelu/nIjbM8sML13LLcUbvvakMSBTJTEeSVGhcCxGRNYzTfLcR5g9e3eXnTQ9JrY1QHFZNfn/rVokSUlS+jBKgeKXuqZ61tQVqwAZcUSBEFoE2zeLlqmlICJDp/d1IsV0/1vr3XCw6wbesG4zkkubxPGpf244QQTYglRIU51tWjZJByWPjrcKkEhJToE1ky9QFZs4nSNxXQf/GmbKRYP68B9t96Q4GEPjI/7+IaeFt+bkVsKw99czh73bRHH4gcf/32nRVzh17f2tWrPRTQ81HmCIAiCaDA2HsuHj5YdZrFenmB/dpFDUYddCbY+MxpGtDO7PzF7NX3afJOo6908Fv64dyCLF/v8pt5uiToEG9tjYV1bos4ekSGBrOjw47+ZhRTyxS19bFoQ8fUhbZqwOnscW6IOrZEiC/dkw5kiy+zcSz4yJ0cMbtMYruydBo8aW2hd1TuV9VclUed7UPIEQRAE4VZLrhu/2ACVNXUQFRIANw5oofr/eGPhAVlrXI9mMcwd2qpJBIQbCwDPurEXDH9juWzdtd8nD2T3PZpZih5P8sAFreGDpYetXi+pqGaWRBGMpUO3qyOUFDu+fXBL2JRh+f2nCspYPTjeFqyw3GD14+Va2PaObAOTh7dq8CLIhHqQxY4gCIJwiq0nzpnittYeyWOiDnnmrz0s3gvj4dTiTFEFLNlvSIZ49fIurCzJumkXsG4H941oDV1TY0yiDgkO8Ic/7h0ED0q6FLx9lfJ2V2qCxYk7pZhdZ0+Ma8fuj5wttfgclkhRIuqQqNBAq9eWPzbc4vnYTonwwiWd4Jo+5sQQrNuH7ly8Tf7eLPoOvjTeogcrZuK6GndIeB+y2BEEQZwnYEIBWmkuaO96wVfsgXr5zLUQGxYIG58aBUckgfnvLzkEKw+ehV/u7s9ElhQUfV2e+9fUXxXLiDw3sZNsJ4WT58pg8GvL2OO2iRFwTV9zJqo90Cr1yJh2MKRtE9h6/BzcOaSlbPuqhgD/72Nj28EDP25j5UlGdkiA12UskANbGRIxlIDJGg+ObAMdk6Pgub/3wL0jWrEeqCjm/t1jcDujMLvJaD3FjOD5u7Jh1aFcWHM4j8Xp8SQLFH5Uj05fUPKEACVPEAShV/BSj/FmyIrHh7vcucBWMoAU7JOKFjUpV85aC5syLEtsIAdeGmchBLF91oT3zSVMsME8tuzy5d+fW8HE3xB7o6JIw5g7d6mprWNdLzAjF7N9Ob9tzrRIihBZ9cQISIszl1YhtAklTxAEQRAWiJ0K7JW/sMfrC/c7/AyvCffGvwdY83ipW1ZO1CFYjgS7QezILGBlSkRRd0H7BJjU0zcbsnNE1+aFXczdJP43oYMqoo67ULHNlyjqkEk9U1lWrJSVj5Oo0yPkiiUIgtA5mK3a5bn/LAr7iuDzovJq2e4LnMM5xTBzue3M1Gcv6sgC8NHt99PGTPbaQz9vh20nCqCqto6JmcQocxzX17f2gdYJESZXK8bpvThvr9X3ju6IJUt6g5748LoeMHJbAosPbIhYNnQHY1KJaClEV3qzeBJ1eoQsdgRBEDrnY4kgK6+utXj+xO87WVspLCsiBa1nl89cA6PeXml67Z2ru5myKBF0keJzLGSbEBli8R6248Jab9d/vsH0HRgjNrxdAuuu8MmNvWxuN1qZ9CbqEBRzl/dMZcK2IXn/2h6mxxjXSOgTstgRBEHonL2nLZvDL96XY3LXYezX7K0n2eMrP14Hu54fyxIkZi47zNymGOy/9YS5S0J8eBBc1iOV3Z67uJNs4D0KMhRz9uLvOGM7JbECv3/vyGLP2yVGwoEzxUwsvj6pqwqjJzj4O1/UJRmq6+pkE1sIfUDCjiAIQuecLbYsTDt3RxYrGxIVEgh3fWduZVVcWQNXf7IONhzLN7327TrLAriipcdWNmXP5rGsmby0hyrSq3kstJE0qX/jyq4sgaChLVjnI+iWDfYjUadnKCtWgLJiCYLQW0eIqz5ZZ3qOYu6lf/a59F2vX9EVruptrommhHHvroT92cUs+eHe4a1YSZPm8WEQE0bdDAhC91mxK1euhIsvvhhSUlJY/MGff/5p8T7qz2effRaSk5MhNDQURo0aBYcOHbL4TH5+Plx//fVs0DExMXD77bdDSYlr2V8EQRC+jijqAvwawbUK68BxLuluaEY/oGU8XOlCqZHZkwfCjMu7sNiu3i3iWNsvEnUE4Vk0I+xKS0uhW7du8NFHH8m+//rrr8P7778Ps2bNgg0bNkB4eDiMHTsWKirMbWNQ1O3ZswcWLVoE8+bNY2LxrrvuasBREARBaAPs2CCCxYSxQwO24JISGRIAO58bY+qKgFzUNRneuao7S27AjEpXsjfx/6GYVNICiyAIHbti8QLyxx9/wKWXXsqe4yaiJe/RRx+Fxx57jL2G5sjExET4+uuv4ZprroF9+/ZBx44dYdOmTdC7tyGLauHChTBhwgQ4efIk+3tHkCuWIAi9MHX2Tvh5U6ZJpH14XU/Te9Pm7DSVJOncNArmPTCEPcaac22eWsAev3VlN5jkwwWBCUJP+KQr1h7Hjh2D7Oxs5n7l4AD79esH69YZXA14j+5XLuoQ/Lyfnx+z8MlRWVnJfizxRhAEoQewfhyC5UJEUYdMGdUWwoL8ITzI36KcCMbA7Xl+LCx7bDhc7uMFgQnifMUn7OMo6hC00Ingc/4e3ickJFi8HxAQAHFxcabPSJkxYwY8//zzHttugiCIhgY9HHuyiqCgvIo9j4+wjmnDZvN7Xxhn032aTq5TgvBZzuuzd9q0afDII4+YnqPFLi3NuawvgiAIrYC14B78aZvFa2iZIwji/MEnXLFJSYYed2fOnLF4HZ/z9/A+JyfH4v2amhqWKcs/IyU4OJj5qsUbQRCEL7Jg12krUYdgrTqCIM4ffELYpaenM3G2ZMkSC+saxs4NGDCAPcf7goIC2LJli+kzS5cuhbq6OhaLRxAEoUf+2n6K9QCd/MNW2feTo0MafJsIgvAemnHFYr25w4cPWyRMbN++ncXINWvWDKZMmQIvvfQStGnThgm9Z555hmW68szZDh06wLhx4+DOO+9kJVGqq6vh/vvvZxmzSjJiCYIgfIldJwth0sdroaq2zuL1+Q8OgY3H8uDdJYfgm1v7NkiTeYIgtINmyp0sX74cRowYYfX6zTffzEqa4GZOnz4dPv30U2aZGzx4MMycORPatm1r+iy6XVHMzZ07l2XDTpo0idW+i4hQ1qaGyp0QBOErtH9mAVRUW4q6VU+MgLS4MK9tE0EQnsEZfaIZYacFSNgRBOEpKqprYdepQjh4phhWHjwLPZrFwq2DWrjUjH1zRj5cMcvcVeL1SV1hYvcUCAmkRAmCON/1iWZcsQRBEHoD181Pzt4Jv24+afXev3vOwP7TRfDuNT0cfk9tXT18ty4Dnpu71+q9r27pAyPaW5Z6Igji/IWEHUEQhAcor6qFB37aBov3WWbzi/y5PQviI4Lh2r5p0Doh0ubnvlpzDF76Z5/V69/d3heGtGmi2jYTBOH7kCtWgFyxBEGoQUFZFdz13RbYeCzf6j2/RgBLHx0Ow99cbvF6xqsXWjzPKiiHsqoaOJ5XBrd/s9nivXkPDIZOKVGUGEEQ5wlF5IolCIJoeCprauHrNRnw0bLDUFRRw15r2SQc/r5/MGvfhS5VJMDfD+LDgyCv1NAdAhn/3ipY8JChZ2tRRTUMfHWp1fdjuy/sDEEQBGELukIQBEG4ADo75u48DUdySuCfXacBbWeHckpM76fGhsLLl3WBYW3NrtIAf7OF7YELWlvEzO07XQTHckshvXE4fLLiiNX/+/ym3iTqCIJwCF0lCIIgnGT5gRx4Z9FB2HGyUPb9u4a2hMnDWkFsuHWfVs5lPVPhq7UZzNXKmfDeKiivrrX67DMXdYRRHS17ZRMEQchBwo4gCMKJkiVYFHhPVpHNz/x4Rz8Y2Lqxw++KDg2EFY+PYJ0jHvp5O3tNKurm3j+YWfk6JFPML0EQyiBhRxCEKm7JrMIKaBoTCnrkXGkVTP5hC6w/ak6GCAn0g9VPXsBi5ZCc4kqIDAmAsCDnLqtjO8n3sp5+cUfokhrt5pYTBHG+QcKOIAinWHs4F16Ytxf2Zxez54+MbgtvLzpoev+WgS1YfFm7pEho1SQCUnxQ7C3cfRpemLsXquvq4WxxpdX7kcEB8M3tfaFxRLDptcQo13qyYlFh7Bgx5PVlFq9f16+ZS99HEMT5DZU7EaByJwRhTVVNHWw7cQ5+2ZwJi/acgeJKQ7anUtZNuwCSoz0n7o6eLWHbtmRfDrx9VTfomhpj87MllTUQ5O8HpwrKYcm+M6w23B2D06F5fBh8svIonDxXbvd/3dC/GUwd3wEiPJDE8Pmqo/DK/H3wvwkd4I4hLVX/foIgfBdqKeYiJOwIwpKa2jq4bOZa1gpLBIUNiiQOllOzdSVpEhkMyx8brkpGZ05RBavdhla0j1ccgUV7s636pa54fDg0jw9nj7G8yLydWfDB0sNwWMhYdYWvbu0DI9p5tsNDaWUNZb4SBGEFCTsXIWFH6J0NR/Pg67UZLAmgWVwYbD1RAKcxNi42FMIC/eHynk1ZpwRsdyUlwK8R60d626B06JgcBX5+jaCurh7q6utZXTZ8vOXEOQgL8ocD2cXwyK87LP5+zdQLIDO/jCUCYOKAs/yz8zTc9+NWRZ/F//HFzb3hxi82wJGzpU7/rwu7JMPbV3dzqY8rQRCE2pCwcxESdoQ33JxYvwxPQv9GjVhh2l7NY5k17HheKZRX1UHnplGw/mgeLD9wFqpq62BQq8ZMgKHlCl2KC3dnw08bTzCLVFRIAFzeMxWu6JXK3Is7TxbCf3uyoUXjcMguqoBPVhx1aTt7N4+F3ycPdOpvcAyP/boDFu7JtngdRSG2wsJWWnKg+PttcyZ0TIliRX6/XZcBGbllFhZCpEvTaBjUujGMaNeEWQUxUxVbeNkCExuwdhxa83A8UaGBkF1YAff+sBW6pUXDE+PaQ3hQAPhjawiCIAgNQcLORUjYEe6CljA8o07kl8GBM8XQqkk4iy+Lk6lntmx/Dtz69SaX/g8G7/dvFQ+L9truQ2oPzF4d1q4JVNfUQdvESMgproD5u7KZUERaJ0TA+M5JLPEBsz8HtGwMSdHOJwfg5eWmLzfCqkO5Vu9hksXU8e2ZG5dbxjCW75avNkFhebXs92EbrSt7pULP5rFM2Elbav27Jxvu/m6LVWFfqgFHEIQvQ8LORUjYEQjGZP244QRk5JbCZT2bwqlz5cy6dEP/5qwrgNg+av/pYtifXQSzVhxlXQNsgTFpPZrFMDcliqfdp2zXQeOguxJjrmrq6iExKpiJLPwfBWXWoge3q11iJBNh2FjeHjumj7HpCkV3KrpY1QS/E7Nmt544B2uP5Cn+OxTDTSKCmaBEV3HzuDC4c0hLRdtXWFYNf+84Bf5+fnBt3zTqqUoQhE9Dws5FSNjpEzzEMcB+1aGzhucA8Pf2LKipq4OI4EAmhiJDApm1beWhs3BUQUxW+6RIOFNUAedkRJZoFeMWMHsse2w4u6+tq4Po0CA4XVgOMaFBkBYXykQdxqvxmDYEx3HjFxvZ49BAf9j09CiLLE1sPI/iFEuNoIULRdFL8/axhIPHxraDvulx4E1ySyqh90uL7X4GC/NSDTeCIAgDJOw89MNlFZQzq8P4zsk243AwC2/L8XMsvgnrWp08V8YmWuz9jWIArS6xYYEWFgS0aKDrDifgQH8/j47xfAFj1VC8YesntBKVVVm3aXIEiiJ092Hs2ubj52Q/gxY4jJNDAYaFarE3aJPIIGidEMmsYuhSzC+tgjf/PcBcsxM6J0HLJhHsOMG4sD4t4iA0yN+lgrmzt56Eq/qkQVSI84kI3ubI2RJ4fu5eWHnQILaRycNbQXp8OAxq01i3hY4JgiBcgYSdSj8cCq7dWYXMFffekkOmgqxyxIQFQoCfH7NGOCI4wI/FFaG1SPx8SnQIPDiyDfuu1NgwaJMYYYo9QmsSZh+GBPhbuKK2ZxbAqoNnobKmjlmeOjeNNtXiQsExtnOS5idJdGli4Hvj8GCoh3rWVmlHZgHkl1Yz4YSxXgmS4q/VtXXsM9hnE8VTUIAfK4VxtqSSuSoX7LYM2Oc0jghigguFNv4u6MIMC/aHk/nlTKxj4kK/lnHQPsnyxMkrqYR3Fh9k8XJoheucEg3J0SEwoFU8KzBLuAYe12j55OVJCIIgCGtI2Ln5w9348TJIjI+F37acVOV7sTp9YXkVExS5JVWgFi2bhCtyG6JgHNKmCQuIn9QrVTaQn1NeVcsC6TEGDCfctUdyYd/pYmYBwyD7y3o0hQvaJ1h0E1ASl4WxYTOXHWZtl3g/THQfosi1JcI4KILx21GMYXHZWiyv4deIiVlHXNg1mTVjx6zQ8CB/irUiCIIgfA4Sdm7+cGlTfgW/4DCL97C8xGNj2jGRhm6kXzZlGi1vjZhlDC03aF0qrqhhsUGbM/KZCEELWlpcmIV1Cks3oMUJXbvLD56FNgkR7HNYpwtrjLkCijV0+SFJUSHMgoXuXUegdXBsxyQ4U1zBymkoBdtIoZbbe7oIFu/NYb8Flo/A7UAXJromi8qrWY00aXFbe6DYQ8sZJgJg0DzGk9mLY+vfMo4lNuDvji7ulo0jICo0AGLD0B1q+F0JgiAIwpchYefmD9f2id+haUI8i13CBt13D1WWiacGKPyqa+tZbNh7iw/BoZwS5vJ76sIOzP2Hli+sTRYe7M/ck9iTs1tqDBNDGHeFAqdZfJjJkvby/H1MiGK9LnuuZCkokrqkxrDOA+guQxclCthv1h13a3wPXtAa2iRGMiscZnzuzSpi24V1167snSb7Nxjjhr8HCsWRHRJNIhZ7kZIblCAIgtA7RSTsXEPvWbHFFdXw3frjsDOzkFnUMFYMi+NebRRU0WGBzNqGVfexk4AcGNP31ZpjcOhMCUsAwFpoI9snMGGJYg3rlWHcIC+siyIMszPzSqugW2o0xITZdgMTBEEQBGENCTsX0buwIwiCIAhC3/qEamsQBEEQBEHoBHNVU4IVsuXKmCAIgiAIQgtwXaLEyUrCTqC42JBckJYmH8RPEARBEAThTZ2CLll7UIydQF1dHWRlZUFkZKTu6p2h2kfBmpmZqcv4QT2Pj8bmm+h5bHofH43NN9Hz2Orr65moS0lJAT8/+1F0ZLETwB8rNTUV9Awe7Ho74M+X8dHYfBM9j03v46Ox+SZ6HZsjSx2HkicIgiAIgiB0Agk7giAIgiAInUDC7jwhODgYpk+fzu71iJ7HR2PzTfQ8Nr2Pj8bmm+h5bM5AyRMEQRAEQRA6gSx2BEEQBEEQOoGEHUEQBEEQhE4gYUcQBEEQBKETSNgRBEEQBEHoBBJ2BEEQBEEQOoGEHUEQBEEQhE4gYUcQBEEQBKETSNgRBEEQBEHoBBJ2BEEQBEEQOoGEHUEQBEEQhE4gYUcQBEEQBKETSNgRBEEQBEHoBBJ2BEEQBEEQOiHA2xugJerq6iArKwsiIyOhUaNG3t4cgiAIgiAIqK+vh+LiYkhJSQE/P/s2ORJ2Aijq0tLSvL0ZBEEQBEEQVmRmZkJqairYg4SdAFrq+A8XFRXl7c0hCIIgCIKAoqIiZnjiOkXzwm7GjBkwZ84c2L9/P4SGhsLAgQPhtddeg3bt2pk+U1FRAY8++ij8/PPPUFlZCWPHjoWZM2dCYmKi6TMnTpyAyZMnw7JlyyAiIgJuvvlm9t0BAcqGyd2vKOpI2BEEQRAEYcs1eiinBKJDAyExKgQaCiVhYppInlixYgXcd999sH79eli0aBFUV1fDmDFjoLS01PSZhx9+GObOnQu//fYb+zy6TS+//HLT+7W1tXDhhRdCVVUVrF27Fr755hv4+uuv4dlnn/XSqAiCIAiC0BMV1bUwb2cWjHt3FYx5ZyXM3noStEajepSdGuPs2bOQkJDABNzQoUOhsLAQmjRpAj/++CNcccUV7DNo3evQoQOsW7cO+vfvDwsWLICLLrqICT5uxZs1axY8+eST7PuCgoIUmTqjo6PZ/yOLHUEQBEEQyNniSvhhw3H4bt1xyCutYq8FBfjBHYPT4Ylx7cHTOKNPNOGKlYIbjsTFxbH7LVu2MCveqFGjTJ9p3749NGvWzCTs8L5Lly4Wrll016Jrds+ePdCjRw8vjIQgCIIgCF8kp6gC/tl1GhbszoYtx89BbZ3BDpYSHQKX9WwKtw5Kh8YRwaA1ArRYcmTKlCkwaNAg6Ny5M3stOzubWdxiYmIsPosiDt/jnxFFHX+fvycHxurhTVTEBEEQBEGcv2zPLIAPlhyCZQdywKjlGF2aRsPtg9Phwq7JEOiviUg23xB2GGu3e/duWL16tcf/FyZWPP/88x7/PwRBEARBaJudJwvg/SWHYfG+M6bXuqXFwMVdk2FUh0Ro0TgcfAFNCbv7778f5s2bBytXrrSo05KUlMSSIgoKCiysdmfOnGHv8c9s3LjR4vvwff6eHNOmTYNHHnnEKp2YIAiCIAj9U1lTC0v25cDXazJgY0Y+e82vEcAl3ZvCvcNbQZtEx+VFtIYmhB3mbzzwwAPwxx9/wPLlyyE9Pd3i/V69ekFgYCAsWbIEJk2axF47cOAAK28yYMAA9hzvX375ZcjJyWGJFwhm2GKQYceOHWX/b3BwMLsRBEEQBHH+kJlfBr9vOQk/bzoBZ4oMIVmB/o1gXOdkuG9EK2if5LsJlAFacb9ixutff/3Fiu/xmDjMAMG6dnh/++23M+saJlSgWEMhiGIOEycQLI+CAu7GG2+E119/nX3H008/zb6bxBtBEARBnN8UVVTD3B1ZMG/HaVh3NM/0enx4EFzROxVu7N8cUmPDwNfRRLkTWwX3vvrqK7jlllssChT/9NNPFgWKRTfr8ePHWRYsWv3Cw8NZgeJXX31VcYFiKndCEARBEPqhrKoGNhzLh183ZcKKg2ehrKqWvY6yY1CrxjCpV1MY3zkZQgL9Qcs4o080Iey0Agk7giAIgvBtIbd0fw4rT7I54xzsPV1kKlOCpDcOh2v6pMGELsmQFuc71jmfr2NHEARBEARhj+raOjiRXwaHzhQzIXf0bCmsP5oHpUarHCcxKphZ5S7v2RQ6p0SDH2ZH6BgSdgRBEARBaIbyqlo4V1YFBWXVUFpVw9ynZZU1UFxRA8fySuFITgkcOVsCx/PKoEYsNGekeXwYDG/bBHo2j4U+LeIgJSYUzidI2BEEQRAE0eCgi3TXqULYcDQPMs+VweGcEjh0psTUsksJoYH+0CohHLqlxkD75CjomBwFPZvF2IzdPx8gYUcQBEEQRINQXFHN6sYt2nsG1hzJZVY5ObD0SHRoIEQEB0BYEN78ITw4gFnjWjWJgJZNwtl9UlSI7l2rzkLCjiAIgiAIj3I4pxg+W3kM/th+Cqpq6kyvR4YEQP+W8dA+KRKaxYWx+nF4HxUacF5b3dyBhB1BEARBEKpTV1fPujl8vuooLN6XY3odrW3jOiXBBe0ToHtaDARouO+qL0LCjiAIgiAIVWPnsN/qO4sOwv7sYtPrI9snwN3DWkGfFrFkjfMgJOwIgiAIgnCbc6VVMHvrSfhqTQacKihnr2Fs3MVdU+COIek+2XfVFyFhRxAEQRCEy226/tl5mt02HMuD6lpD+ZHI4AC4uk8a3DO8FTSOoLaeDQkJO4IgCIIgFFFZUwtbjB0d1h3Jg1WHcqGq1pwMgUkQ1/drBlf0SoPQIG236dIrJOwIgiAIgrAp5PadLoY9WYWwI7MA/t1zBgrLLUuUtE6IgMt6NIUxHRPZY4qf8y4k7AiCIAjiPAfFWmZ+GeSWVEJOUSWsP5YHe04VwbHcUguLHJIQGQw9m8VC56ZRMKZTErSl2DlNQcKOIAiCIJwo4VGCba4qa1nDeWx3VVpZA2XV2PaqlrXAwpZYCC+qi/e80G54sD/EhgdBVEigV8dxPK+UlSBZuPs0HMguhqKKGpufjQsPgs5No6FTShQMbt2Y1Z3zp6LAmoWEHUEQBHFeU19fzyxWZ4oqoaK6Fipr6pgLsrIa7+sgr7SSNZhHd+TuU0VQXm3ZZN5Z0FPZpWk0DGvbhAkl7GfaEN0T0Bo3b0cWzN15GrYcP2f1fnx4ECREhUBceCB0TY1hZUlaN4mEtLhQcq/6EI3q8YgmGEVFRRAdHQ2FhYUQFRXl7c0hCIIgVK6vtjerCHaeKmA9SU/kl8HJc2Vw6lw5lBqtbEpBixWzyGG7q2B/9phZ5Iz3CGtgX1kLJWjRq6ph/wOb2Uv/F7bJuqRbCkzsnsLaZKkponCK35RxDr5cfQz+3ZsNfMZHHdmreSyM75wMA1vHQ1psGLMuEr6vT5wWdj169FB80G3duhV8CRJ2BEEQ+iIjtxSW7s+BlYfOsmzO4krbLsfYsEAmyoID/CAowA+CA/3ZY3SbpjcOgw7JUdA1NRpSY8PY664KsDNFFbDiwFnWKxX7pqLw4yRHhzBxh9mlrRIimOhrER/uVE9UrCG3OSMftp0ogP/2ZENWYYXpPRzDZT1SYGK3ppAUHeLS9hPa1idOy/NLL73U9LiiogJmzpwJHTt2hAEDBrDX1q9fD3v27IF7773XlW0nCIIgCLeoqa2DZQfOwqcrjzBrlQjGuvVsHgvtEiMgvXEEpMaGQlO8xYRCSGDDlOdIjAqBq/qksRvWgVu89wz8tT0L1h7JhdOFFey2+nCuxd8E+fux/qloVQsPCmA9VptEBjNLIVJXD3C2uBKO5pZAZr6hODAHPzOhSzLcNigdOqaQ0ULvuOWKveOOOyA5ORlefPFFi9enT58OmZmZ8OWXX4IvQRY7giAI3wRj45YfOMvE0aK9Z5g4QtCo1j89Hka0bwIDWzVmljCt9ibFJAysD3fsbCm7z8grheN5ZSxbtQaVmxNuYkx26NI0Coa0acJi+RpKtBI+6IoVwX+yefNmaNOmjcXrhw4dgt69e7MN8CVI2BEEQfgOmOCw5nAuzNt5Gv7dnW0Ru4aZnJf3aAp3DGnp8y5HtEBmF1VAcUUNE384Tkz2yCmqYMkdXMBihwe0QKKo83bWLeFDrliR0NBQWLNmjZWww9dCQnz7RCIIgiC0BdohjpwtgQ3H8mHD0XxYsu+MhZjD+LRRHRJhUOt4GN4uQTdWKrQwYlwfQSjBLWE3ZcoUmDx5MkuS6Nu3L3ttw4YNzAX7zDPPuPPVBEEQBMFAV+TC3dkwZ9sp2He6yKpY7vjOSSyGrKHKhhCEboXd1KlToWXLlvDee+/B999/z17r0KEDfPXVV3DVVVeptY0EQRDEeQa6H//ZdRp+2ZQJ647mmcp0YBJBn/RY6J4WAxe0T4QeaTEk5ghCgOrYCVCMHUEQhPfA6WjriQKW/DBn60nIKa40vde3RRxc1C0ZLuqawuLnCOJ8oqihYuw4VVVVkJOTA3V1lv3kmjVrpsbXEwRBEDoFkwHWHsmDFQdzYNn+s6wGGwcF3A39m8OVvVIhLY5izAhCCW4JO8x+ve2222Dt2rVWqy4s3Fhb617bFYIgCEJfVNfWwf7TxawsyYqDZ2FTRj5U15odRyGBfjCiXQJc2DUZRndMhOAAfSRAEIRPCLtbbrkFAgICYN68eayeHfWSIwiCIKRtvHaeLGAdFlYdzoX9p4tMJTo42It0eNsEGN7OUGsu1Fh0lyCIBhZ227dvhy1btkD79u3d+RqCIAhCR7Xl9p0uhu0nzsGWEwWw/mge64ggEhUSwPqUDm3bhJUlaREfRoYBgtCCsMNWYrm5lm1PCIIgiPMzg3X+rtOw+lCuVZP7yOAAGNK2MctiRUHXPC6MMlkJQovC7rXXXoMnnngCXnnlFejSpQsEBlpWuqbMUoIgCP1yOKcEfthwnHV+EK1ysWGB0C0tBno2i2VCrneLWIqVIwhfKHfi52fotyc1oftq8gSVOyEIgrDPibwy+G9vNisYvPn4OYsM1uv6NoMxnRKhc0o0WeQIwhfLnSxbtsydPycIgiB8gMKyavh3Tzb8ujnTQsyhdsMYuUk9U1kGa1CAYbFPEIT3cEvYDRs2TL0tIQiCIDRDeVUtE3O/bznJEiBq6upNYq5fejyM7JAAYzslUX05gtAYbhcoXrVqFXzyySdw9OhR+O2336Bp06bw3XffQXp6OgwePFidrSQIgiAarC/rd+uPw+wtJyGvtMr0ervESJjYPQUu79kUkqNDvbqNBEF4SNjNnj0bbrzxRrj++uth69atUFlpCJ5FHzAmVMyfP9+drycIgiAaCEx+eG/JQfh180moMtaZaxoTClf2ToVLujeF9Mbh3t5EgiA8LexeeuklmDVrFtx0003w888/m14fNGgQe48gCILQfkuvj5cfgS9WH4PyakPCW58WsXD74JZwQfsEipsjCB/DrTP2wIEDMHToUKvXMXOjoKDAqe9auXIlXHzxxZCSksIyav/880+rTNtnn32WdbgIDQ2FUaNGsZZmIvn5+cx6iBkjMTExcPvtt0NJSYmLoyMIgtAvFdW18OnKIzDw1aXw4bLDTNR1aRoN393eF369ewCM65xEoo4gfBC3ztqkpCQ4fPiw1eurV6+Gli1bOvVdpaWl0K1bN/joo49k33/99dfh/fffZxbCDRs2QHh4OIwdOxYqKipMn0FRt2fPHli0aBFrc4Zi8a677nJhZARBEPqkuKIavlx9jAm6V+bvh8LyamgWFwbvX9sD/rpvEAxp04S6QBDE+eqKvfPOO+Ghhx6CL7/8kl0IsrKyYN26dfDYY4/BM88849R3jR8/nt3kQGvdu+++C08//TRccskl7LVvv/0WEhMTmWXvmmuugX379sHChQth06ZN0Lt3b/aZDz74ACZMmABvvvkmswQSBEGcj+A1dMfJQuZuXbj7NFTXGjJcU6JD4L4LWsNVvdMg0J+scwQB57uwmzp1KtTV1cHIkSOhrKyMuWWDg4OZsHvggQdU28hjx45BdnY2c7+K7t5+/foxIYnCDu/R/cpFHYKfxyLKaOG77LLLrL4Xkz14wgcvAEgQBKEXMAli4Z5sZqHbnmkOj8HerLcPTodr+zaDABJ0BKErXBZ22FVizZo1cN9998Hjjz/OXLIYz4b9YyMiIlTdSBR1CFroRPA5fw/vExISLN4PCAiAuLg402ekzJgxA55//nlVt5UgCEIL8XOzt56Ez1YehYy8MvZakL8fjO+SxARd19QYb28iQRBaE3b+/v4wZswY5gJFSxkKOl9j2rRp8Mgjj1hY7NLS0ry6TQRBEK6SX1oFv23OhG/WZkBWYYWp1dcN/ZrB9f2bQ2JUiLc3kSAILbtiO3fuzAoTYzFiT4JJGsiZM2dYViwHn3fv3t30mZycHIu/q6mpYZmy/O+loNsYbwRBEL7MwTPF8OnKozB/12koqzKULEmIDIa7hraEq/qkQVRIoLc3kSAIX6ljh/F0L774IvTq1Ytlqoo4alSrFBSOKM6WLFliEnJoXcPYucmTJ7PnAwYMYCVWtmzZwrYFWbp0KYsBxFg8giAIvbH7VCHMWnGECTpjxy/WIeLmgS3gku4pEB7sdnMhgiB8DJfO+hdeeAEeffRRlnGKTJw40SI9HjOw8DnG4SkF4/PE0imYMLF9+3YWI9esWTOYMmUKE5Jt2rRhQg+zbjHT9dJLL2Wf79ChA4wbN45l6mJJlOrqarj//vtZYgVlxBIEoRfq6uph3dE8+GzVUVh+4Kzp9ZHtE+D2IenQPz0e/LChK0EQ5yWN6lGFuRBfd/r0aRZfZ49hw4Yp/s7ly5fDiBEjrF6/+eab4euvv2Zicfr06fDpp58yyxz2oZ05cya0bdvW9Fl0u6KYmzt3LsuGnTRpEqt9pzSZA62AmG2LLdHUsjYSBEGoQWFZNXy3PgO+WXectf/ijO+cBPeNaA2dm0Z7dfsIgvAczugTl4Qdiia5LFRfh4QdQRBaY29WEas/N3dHFlTVGnq4hgX5M1frXUNbUQ9XgjgPKHJCn7gcgEGVyQmCIDwDrre3HD8HHyw9DCsOmt2t7ZMiWbmSid1TIDjA36vbSBCENnFZ2KEL1JG4Q9coQRAEoYzaunpYtDcbPlp2BHadKmSvBfg1gjGdEuG2QenQu0WctzeRIAi9Cjss7ItmQYIgCML9DhF/bT/FEiIOnikxFRS+sGsy3H9Ba2jVRN2i7wRB6BeXhR1mm+otxo4gCKKh+XPbKXhr0QHIzC9nzyNDAuC6fs2YyzUhkgoKEwTRAMKO4usIgiDc4+jZEpj+9x5YdSiXPW8cEQy3DmoB1/VtBrHhQd7ePIIgzidh50IiLUEQBAEA206cg4+WHYal+3NYUWGMobt7WEuYPLw1RFBBYYIg3MSlqwh2cyAIgiCUUVlTC6sP5cIPG04wQccZ0qYxTL+4I7ROiPTq9hEEoR9oeUgQBOGhDNeNx/Lh9y0n4Z9dWVBRbVgQ+/s1gkk9m8KdQ1pCm0QSdARBqAsJO4IgCJUoKKuCJfty4L+92bD2cB4UV9aY3sMYuou6JsNNA5pDS8pyJQjCQ5CwIwiCcMMqt/tUIaw9kgebMvJh1aGzUF1rjkGODg2EcZ2S4MreqdCreSwlnhEE4XFI2BEEQSigsLwajuWWsmxWvD94phjWH81nr4tgd4gxHRNhRPsE6Joaw1yvBEEQDQUJO4IgCIHTheWw73QRHMgugQwUcrkGIZdbUiX7ecxkHdAqHno3j2Viri3FzREE4UVI2BEEcV5TUV0La4/kwr+7zzBXalZhhc3PJkYFQ3rjcBYj17JxOPRoFgPdUmMgwN+vQbeZIAjCFiTsCII47yirqoHlB87CPztPw/IDOVBaVWt6D12nrZqEQ/ukKKOIC2ctvVo0Dqc6cwRBaB66ShEEcV5wIq8MNhzLg+UHz8Ly/ZZiDi1xYzomwaiOicylGk4CjiAIH4WuXgRB6ArsjHO2uBJO5JfBvuxi2Hb8HGw5cQ6O55VZfC41NhQu7JIM47skQ9em0eBHSQ4EQegAEnYEQahCTW0dFFfUQFFFNRSV8/tqqKypg5q6eqit4/f1UFNrvJe+bvG+zOv88xZ/j/d17L6kshZO5JVaWOM42LqrW1oM9EuPgzGdkkjMEQShS0jYEYROW1ih6zEjrwwy88vg5LlyOHmuDLKLKiCvpAqqa+sshBG/IX5+KIL8ADUPxpvhza9RIyaM/ITn+B1VNXXsHsVbmYyY8ha47SkxoSzJoXtaDEtyQBdrZEigtzeNIAjCo5CwIwgfo66uHvJKq+BMUYXxVgnZheVwqqACMvJKmQsSXZEuw/SZ6/2gw4L8WWHeqJBAiAwJgNAgfyYGURga7v0sn/vbeJ3d+wnvS163+vtGEBzgD83iwyAtNgyCAihTlSCI8w8SdgTh5XiwoooaOFdaBefKDLf80mrWmiqfvVbN3ssvqzK+ZngPLW2OwAzOFo3DoFlcGKTG4i0UkqNDoXFEEBNAXBD5NzLeG92SaLmrqzdY81BE1tYbrHl1dcBcnvge/vtAfz8I9Ecxhfd+zBqGQg4fEwRBEN6BhB1BqCTQUIidLamEc6XVUFhuEGH5pZXsnsebYQxacaXhvqSiBgrKq00uUGfAzlTYexSzOZOiQiAxKoS5HpvHG4Rc05hQiAsPohZWBEEQ5xkk7AhCoeszu7CCdSXAOLXT+LignN3z5xhv5irhQf4QExbExFhMWCC7jw0z3sIDLR7jeyjqyDJGEARBSCFhR5y3YNA/WtlySyqhoAyta1WQV1JpEG0o2PC+qBzOFFZCVa0y0RZvFGYYY4YCjAk0fC00iLkpo0IN7sqokABWKw1fx8+HBPp7fLwEQRCE/iFhR+hSsGHyACYW4H2O8XamsALOFBsEGz5HIacU9Gg2iQiG5JhQSI4KgaToEEiONtyjC5S7QylgnyAIgvAmJOwInwFdnaI7FIVbdiGKtgqTxQ1j3NACV68wbA3zBUyWtbAgiI8IgqSoUEG04X0oJESS65MgCILQPiTsvMgzf+6G1YdzWWYhWnpQOAThLcAPQgP9WVYjuuvCgv0hIgjvAyAk0A9CAvwhWLw3fpa7+vCzvlB4Fft1Yk21fGPWZ77xMcaz8aQDw73hNUw4UAqWvkAx1oTdQiAhKhgSI1GkBZuEGt4wro1ngxIEQRCEr0PCzotgHNex3FLVvxfdhijuUBRGGGO5IoL9IQzFYZC/sV4YFp813PP6YaabUP4Cb/h9aAHjRWwN5S7wMRgeG0ti4D0meJofmz+DpTMKy42lO5hQq4SKaueTDbC0BlrT0O2JN3ycEBUCceGBTKShuxRfx1g3XxC3BEEQBKEmjeqxTgPBKCoqgujoaCgsLISoqCiP/78jZ0uYyKmuqYPK2jp2j0H6VcYq/qWVNaw1Et6jdQvbJVVW10IFfl68r66Fkkps4VTjVmamN0DrJIow7g6NNyYbGF4LNrwWYX4PkxKohAdBEARxPlHkhD4hi50XadUkAlo1Ub+VFKuVVlHDBCGrl4YCkYnDWiYQ5VpJ8SK04o0XqEWLm8FyhxY8YBY9w2OzRY9b+djrxs+ZPtPI0IoKM0ENIi0Y4rC0R0QQK/NBQo0gCIIg1IGEnc7AjgLBEf6szhlBEARBEOcXlOZHEARBEAShE8hiJ8DDDdGXTRAEQRAEoQW4LlGSFkHCTqC4uJjdp6WleXtTCIIgCIIgrHQKJlHYg7JiBerq6iArKwsiIyN1F9CPah8Fa2ZmZoNk/DY0eh4fjc030fPY9D4+Gptvouex1dfXM1GXkpICfn72o+jIYieAP1ZqairoGTzY9XbAny/jo7H5Jnoem97HR2PzTaJ0OjZHljoOJU8QBEEQBEHoBBJ2BEEQBEEQOoGE3XlCcHAwTJ8+nd3rET2Pj8bmm+h5bHofH43NN9Hz2JyBkicIgiAIgiB0AlnsCIIgCIIgdAIJO4IgCIIgCJ1Awo4gCIIgCEInkLAjCIIgCILQCSTsCIIgCIIgdAIJO4IgCIIgCJ1Awo4gCIIgCEInkLAjCIIgCILQCSTsCIIgCIIgdAIJO4IgCIIgCJ1Awo4gCIIgCEInkLAjCIIgCILQCSTsCIIgCIIgdEKAtzdAS9TV1UFWVhZERkZCo0aNvL05BEEQBEEQUF9fD8XFxZCSkgJ+fvZtciTsBFDUpaWleXszCIIgCIIgrMjMzITU1FSwBwk7AbTU8R8uKirK25tDEARBEAQBRUVFzPDEdYo9SNgJcPcrijqtCLutJ85B05hQSIwKAb1x6Ewx+Pk1glZNIkBvnC4sh7PFldA1NQb0RkFZFezPLoZ+6XG6DFk4nlcKZVW10CFZG9cANTmRVwYllTXQMUV/Y8stqYSM3FLo3SIO9EZpZQ3sOFkA/dLjwd+vkS6vlzlFldAtTX/Xy4rqWthy/Bz0aREHQQHupzUoueZS8oSG2Z5ZAJfPXAtDX18GerxQjX5nJYx8awXU1NaB3hgwYylM/HANHDlbAnrj4g9XwzWfroe5O0+DHuNYhr2xHMa/t4oJWL0x9I1lMOH9VWzRoTfwOnnFrHWw9nAu6I3bvt4E1322AT5bdRT0CF4vL/loDRzV4fXy8d93wvWfb4BXF+xvsP9Jwk7DLNqbze4ra/QnfMSJpbq2HvTKnqwi0BuZ+eXs/t/dhuNTT5wpMh+XBWXVoDfRysk8VwZ6A62syMpD+hN2G47ls/tfN2WC3qgS5rcjZ0tBb8zdkcXuv1xzrMH+Jwk7DZNbrD+LAaemznwy1woTjt4m0CB//Z5iargVtEZGnnli0ZuXWVwgBjrIqvNlgnV4XOr5nBMXGbFhgaBXAv0b7oKiv6NER5wt0Z+7RM5KV6szi504gQYH6vcU06Noxfg6Tk1dve5ifTgBDTjJNDR6FD96HhvGRXJqdXbOeet6qb+jRGfBwHqlWoirE613eqDc6BJCgnUofnQ9yeSV6XaSqaiu0601UrSS69lip8ex6fmcEwlswH2nv6NERxSV6yvGR+TkOUOclh4tI6VVNabH+hqZ/ieZXCH2s0ZnluQT+WW6HVuVsFDU43HJCQ7wBz0bMKp1NheIkMWOsAgG1iP7TxfpVtiJFju9jU0MdNajxa6oolq31oP92UW6HZt4zunxuNTz2Iotzjl9eW9EAknYucZzzz3HaryIt/bt24MeLlZ6Q8x+0luMXUG5fi9Uep9Ai8rN1tZqne27Izklug1/0FsG8/kU1yqec3qzJNcLIQKhQQ1nbdVdgeJOnTrB4sWLTc8DAnx3iMWV5gNeb2QXVeh2kjmQXazbC1VxpXkC1Vkys1XCkt6sWuLY9HZcHrIQrfq1kjdknJY3Sl/p7ZzLNJaGQlrEhzfY//Vd1WMDFHJJSUng6xwWLlRIXV0969KgB8qqalglbr2ezE//uVu3Y7v3h60W+1FPnCmqsDjv9CR+8Poxf1e2bo/LO7/drNuxPSNcT/QGdkFZdzRPt6J8zLsrZK13nkZ38v/QoUOQkpICLVu2hOuvvx5OnDhh87OVlZWs/5p40wqj3jYfEHqr9Tbl5+0Wz/V0Mh/OMVvr9DY2zGTeebLQ4qKsJwbMWGLxXE8C4au1Gbo9LvNLLet96kmQoxj4ZXOmbsNz7vhmk27PufKqWotM9IaMmdeVsOvXrx98/fXXsHDhQvj444/h2LFjMGTIECgutpxsOTNmzIDo6GjTDRvsaoFMIXtNbwc8Xqj+23tGl2NDbvh8o27H9sP64xbPiyv0I+xyiipAuqv0FCLwxr/7dXtcTv5+i27HtnR/jsXzEiEUwtfBln3rjxo6auhxwfHUH7ssnpcJdSQ9ja6E3fjx4+HKK6+Erl27wtixY2H+/PlQUFAAv/76q+znp02bBoWFhaZbZqY22rVc+tEau3XffJmZy4/odmxbT5yziB3U09iwn+9zc/davKYni919P5pdzHoTCNjSSLQc6GkCzSooN7Xb0tvYkNu/MbuY9baYevavPVav6aVveFlVDczZdsritYoGtNipGmP3/vvvK/7sgw8+CJ4mJiYG2rZtC4cPH5Z9Pzg4mN20RGF5NeRJXAt6mmTe+PeA6TGGDOKw9DK2az9db/WaXsYmuoM4JTqZZHAfbcowx3y2SYhgwfh6EQgP/LTN6jW9ZGtP+cUyrENPY9soEax6W0z9beyhirRsHA5Hc0t1c869Mn+f6XFkcABLhCyrrvFNYffOO+8o+hyWIWkIYVdSUgJHjhyBG2+8EXyFo2fNwdvtkyJhvzHDUg8HvPSi1CwujFUd18PYpK3EejWPZQkiehnbpyuPmh5PHd8eXl2wXzeTjNTKGhsWpCtRLtK5aRTsPlWkm+NSFD8DWsazQHy9jO3L1ceszzmdLKbE9nZIq4QIJuz0cs4t3mt2oT85vj1LqCuvqvNNVyzGtCm5HT1qniTU5LHHHoMVK1ZARkYGrF27Fi677DLw9/eHa6+9FnyF0krzAf/Pg0MgwJgJq4cDXrwoHXhpnKmKuh7GhoQb6xR9d3tfSIoK0dXYYoxi58lx7dkEqie3kHhcHnp5vKmPqh4EgujaWjftAogJ1ZdoTW9sKCHx6uVdoF1SpK7Gxo+/6/o1g4u7peiqBJaYSLDvhXEQGuivm3MOaRobyu4fGtkGhrRpzB6XN2AVAV3F2J08eZKJuHbt2sFVV10F8fHxsH79emjSpAn4CpU1hgO+W2o0+Ps1Mh3oephE+dhQAKGoO2K0Tp48Z50s4sttjVonRLB9h7y/5BDogUrjChstPhEhBkP/qYJyXcTE8OMyJTqEVYc/XWiw4B0+I5905auttqJDA+F0oaGu1kEdjE08LjumRJnOuQ+WHm7Q0hKePi77tIiFiOAAU027czKhOr46Niy4jIV7eVH3HZkFoAcqjePr3izGJFpLq2otahL6rLBDoTVz5kyYOnUqPPLIIxY3T/Dzzz9DVlYWK2OC/xuft2rVCnxxJSPtCfj5KuetnKsP5WrqROGuSl5kk4vWJ2dbZg8pYfepQlhx8CxoqU5YtbHMAu47fqHCeMk8oTCsEo7nlbL4Ey1NTjzuE8eGMSOcv7ab42SUsmTfGdgntJTzNryERLDxAnws19AV5f2l8rG59thyPB/WHTHX5fI2lULSBE6ivOPLR8usk5iUlPJZuNtcC09LRZfxuBQtdbtOmcvyKK1hOHvLSU0tVDDemo+NCzvkjf/MccpKWbj7tFVtVG/Ck3l4X9+Vxmu5GHenlD1ZhbBMkj3sbfJL+PXSIFw5P2+yXX5NDhTxv285aeW69lqB4iVLlsDEiRNZPbn9+/dD586dmYsUJ6uePXt66t/6fPo3D3Q+KKmHhtYRZ8gproAbvtjAHh+bMYHFNXpb+MwyZsSq0f7nog9Ws/uljw6Dlk0iwNssO5Bj0Wpr3ZFcWauJEq75dD2zGpVW1sC1fZuBt8nILTVVh0erCLfY8axEZ0BLEc/0y3j1QvA2GCd4tTHphQs6V0FhMenjdezxtmdGQ2y4we3pTXBS4AS42Y5q1Nsr2f33t/eDwUb3kjfBCd28mPKDbSfMCTDOromwZMrWEwVwNLcEHh/r/TaUKDR5zUi0/nBrJHLISWsrLjTu+X6rZs45FCm8fp0aruUL3zfMBQseGgIdkqPA25zIK4Mso9Xfr1EjCAsKsFvKzB5P/bmLFRZfezgXnhvf0vsWOywlgjFvu3btgpCQEJg9ezYrJzJs2DBWkoSwZvQ7hgunnPhp5aR4KRT+XgtB7t+sy7BK/1aDfae971LanJFvUZYAJ5lhbRNcLpjKXYFfrTEHT3uz+OvwN5ebntfV15tcC0hchHPiRbywodj3Ntd9Zp3J7CpiaZuT55wTvJ4ArTQvC9l5arHuqHnR4i3Qqs0ndASFT/e0GNNzZ2O1UNS5aslUGzyO+r1iLpZ9psjS4u9sayr0bmiJ+3/cZtErXC12CcXTvWmcGfrGMot9KYryRGPstVJ4txhn506PCbt9+/bBTTfdZGrzVV5eDhEREfDCCy/Aa6+95ql/q5ueec9e1JHdhxnNuJ2bRjv1XeLqXAsNsp8XaqDxxII7Bqez+2FtXY+BPFfm/XiTPyQnHcZpvXxZZ9NzVwOCD57xvutkv8Rl2qtZrIX1NyHSuQtVZEig6bEWAsHFTho3DWjO7h8Z3Zbd924e67KwE3vqeovXFlq77J67uKMpDtRVtHA9WXXIUlymxobCw8b95usJFEVGFyznqt6GwvnxRgtwj2bOHZeBxmQgrSymFu8zF6gf2MqQiPX2Vd0s5gZXKKrw/nF5UHLNHtiqsdVx6gytmrjWX9Zjwi48PByqqgyTbnJyMis7wsnN9f6KT2tIT7iRHRIsDnxnYz/Ez5dqrKfnJd0NGV69W8S5ZFEUY8+cdVF7ArmAWFyZxYYZRIyW4nacRToN8H7FGNDtytjEdsfOxo14mhHtDeccd+c4K8hFMaGF1k+ia7lHM4M1q0uqYYHoThD3CSfdSZ5Auv242MDM7baJES4dl3wBrQWkradiQg3XkX4t41yq0yc6DCqMQf1agS+eeHazaN1yFi0kGFZJjks+nv7GfcdDB5QSISyENSHs+vfvD6tXG0zlEyZMgEcffRRefvlluO2229h7hCW5pZbm9hCjuyvAz7CLXvrHOZeKOCm5kpygJtIkgLaJhrIEMUbhg/XenOnQII7tY5lOFg3Nb0Ick8g5o2VDWifNGbwtCpfsy7ErGvZkOZcEIe47bye/SK064cZYmPBgw7m3PbPAKQuHeNG+R9LmytugpRWJNpY7QXHmqoVDai3zduygnMXkiJPxkryslJi04C2WS84LvpjKMbpkpW24nLmGbDO6nL2FdC5IjQ1j95FCpj3PKHX2+97TQAWCv3ecshl350pST6BwXJ50YkHlMWH39ttvs96tyPPPPw8jR46EX375BVq0aAFffPEF+AoYHN4QpQHe+veg6XG7xEiTLz7f6GpEq5a02bU9xLguW5mxGIeHk5enWSvJEry0R1MLYedsdqWSmDW0Bm3KyPe4S0ZqmZl7/2Crzzz3t3XrHKUUyaxC8UKNY2sIi9eXQpzfe9d0Nz3ONWZ9fbjMucxRcd+9t1j+QpxbUtkgcUGYBSnCrZCRwebjcv1R5Rmu4rFma2WOCTGYOevpjGdpkPYjY9panXMfObnvROQEL1orsGBwQ5R02CuECPxwh2GeEXnmz92uf7fMYgUXng01NnHbn76wg+nx5uOG5JB/dp126vuwzAbn23UZsp/B800MBfIUPJaRc1lPw1wQIZxzv25S3tpTyfW9wjgXNMQi+dfN5mvKh9f1MD3myRRioXcl8JqayH97s70v7DAbFnu2crfsrFmzYOfOnSyJonlzQyyLLzDw1aUw5p2VLMvUUxRXVFu0bPr34aGmxztPmk8EZ1YySmLPJry/ivWlXXXIc5YTnAD+JzRDxmxBbp7mxVKdXSVXK3BFPPTzNrhy1jr4ZKXnLHo4OWNSCGfa+PYmV5dIZr7r7mI5SyZaKXFsD8u0U1KTxXvNsTDIJd0NF2F3OJZrjkGxlcE25LVlLOtZboJVCzyXnpi906IwMY8dDDNa7JByJ8SzkgbtN3+5kWXO/irTok1NxPqJv98zwJSZx916yJEc1wPY5TK9sY3SVZ+sgxfmub6QUcK8neZF4ODWjWFQa/czdMUFFLfYisyYv5+NbbobizQlSEvl3DFEeSakLXYJc0j7JOtzDuuJ4vnWf4Y5YcNjc8Ec81yw+skRLB5Z+ptLk0XsUaFAaD/x+052vXSlfJEziCVXcI67qKsh5MgdxBI1zsQze7xAMcbZYU25EydOWNx8gYYyYd/ylSH1Ww5xhSjWpHLETV9udDiB8vi0WSs8J35mrTwCx41maOmkKVoPnHF5/Sasimzx7x6DKHldJoBcLZYfOMva/HCGtJFPAsHyJ87UChORsxB8YbSiLdid7THLD1rN7vjWnOnbVUawusIzQuPvdknyAfxcTP1lw62hBtOECQbhEwx7bAx/cHbf3fmt2f3a2Ea2MLe6iL+DJ7JhxfCAtDiDu0uaVOVMrJbUcim2z+N8vdawyPl+veeu7xgCgFmVnCt6paqSySgiZ23lluufNp7w6GLjWhWztDnLDpgX7i0am48Fzn5jZQG0fjlbvsgZZi4/DAcE7xdv3YeECyVBap24pknPY7nr4d/G2nieLBaPx9CtX5vn8duNiYHugIt67hlBwoRahl4TdgcPHoQhQ4ZAaGgos9Clp6ezG7pi8d4XEIP6vzFetDzhDsIYM1vMvL6n0/XQpAd3lQNL35rDnimoim5eqbASCy/zOEIkJSbUqQK3It4o5ItuC/FE5tXv5bi6jyGrTQnHci1daHJW2nDhIuhszIYSUGSL5RaQt68yu2F5myNnkY6lqNzazSzuy09WeKb1IBZDnbPVtmhMizMfi/5O1H8UkxUcuew85dLDWB5es8xRiQVpxp49tgo14pz1HqgFutRGCKV3kHGdkyye84SlkcZEGCVILereGBty+cy1Fs9n3WBZ73W6MaPZmWueNFyjusb676JCzdcT0buids3BN/8zhxsh4YJQ4XGECE+AUYLU2+RszVA1wH3R/YVFFq/d2N/SK4m9w5GWTmS54uLamXm8QQoU33rrrazMybx581hWrLcL5LqCOPFgw3pP8OhvO+y+P65zMksBxwB8R5MBnjwYtG19ofJOAP7biyxPZDnQlbL6cK7D5AmswH3lJ+tYkPP+7GKr8YkiUe7EU/v4W7jHcbzDbYPS2UpftAbJgSvlaz9dDzV1dVYxKLxCu0jvFrFwanu5RUC1mmQVllvFrmA7KpHJw1rBjxtOsJp9jn7fR37dzqwCYlwUD0GQIo63m1CXTE2e/ct+/BWOpUvTaCaaHZ072A7v+s83WFilvTXBID8qsChd1qOpVYkeW6IAXVjoVpLG4spdi9AzwDuKYOypWHFfDeQSdbCbhshdQ1vBawv3m3ob2wKP2bu/28IKAe+Q1D+T2+fY4pF/DuMkRVGiBvhbS8cXJTnnrunTzFQ2CksFRdnJmES3+PIDOVblN+TCWMRrr1iOSE0+VOAGHdGuCbMuOsocxdjwK2athUMynTTwuAyWdG3yNHKuY1GoIlf3TmMGnOYKdMS0OTthR2ah1fVSmi3tFYvd9u3b4ZNPPoHx48dD9+7doVu3bhY3X0DMGmsoXfqxYKHjBAf6KVpJTp29SzaeC4ulXv/5epvuTl4fSW2ChMBPW3XBeEsZR2P7fv1xFm8gFXUIruKlMXp9jaVUkIYICpaDd2iQEzAiB7KLYWNGvpWoQzD2ZX+25QkuujB4co2ayCVlSF2LfFLBSdBRWRC0jkkvUsif27Pgkg9XW/w/8ZxrEhEMnkC6tbxunQh3wToSdm//d9BK1HGBesGbyxu8HI9Ys8wWXAw5Ep8oDFDcyiVYDX5tmVWCRvskQ7Y7gh0c1EbOSiWdQJWec+ju/2/vGStRh9z61SZ4XLLgbiXU/TvqgeK6cmE24jUMQaHM92+Jg9IeGKQvVwfzqT92w1Wz1lks3KoEK56Yhakm0l03oYulpRXhgszROffblkxZUYcMmLHUql1hQqRnriP24nCx77T8cem4JMtPGzNlr5fPOhG+4TFh17FjR5+vVycWinQmI9UdRnZItHkhlsuQFLFXvgDdrfskAkHsA+qJuluhgssQuWNIus0JNL/U/oW43kGnhq/XSFzlwvXp8Fn1J5lgiaVAeiKLgjkjz/5E4GjRcPvX5lg36YXPE8elnFCTWuTE2DN7lmRHmWg4sYpBx+I556ni09jmR0QuTosvOKTxV1Ls1Yg8mlsKb9np6+lsD2EliO2LkAdHtrG5UHS04PEXYg2VeBvE48ATnQWUZEDyc85RezhH1zuMURSFpGhFwmQDtUFrvRS5FnAmUe6GFwYXkaL4EQU+7wmtNv6SBYdcq0TTXCDElbkSPjXl5+02F8JHPbDv5GJVpdfLOIXHpVoFpD0m7LC7xBNPPAHLly+HvLw8KCoqsrj5AqKQkluVN9SKm5vKcSXpzIQlRerW47WDEKlVSA3CJa4YORM5n0DRfWJvle2ogKh0ghXdC6c80N5JTEMX09lFeK9QFNX2SuY4KlsitfqIY/OE+FFSTkYUdnPtNO5WklUqXsssz7lSj8RPSidRudOGZ25PnbPLbpiAo4KqUgEhxg/JWWjdJcQo2qTnl5w4wGSH04Xlimq7yYElJEREgYAuarVRUjCaT+Jo0Vkr9GuWosStJS6gqoXHnrDCKi2GzUuXqNluUBybo4WMq0hjVeXOKX6svrP4oN0qCY4EfkG55RgaR5qFnbM1ANXad1zYoXD+Z6ftcjVqhU15TNiNGjUK1q9fz+rXJSQkQGxsLLvFxMSwe19AtIDhhaKsATo4yMUqZQii0t5B7ciIXmlnkvVE1W6p9UAuO1dclYrtnZydZKyChMX2Th4Ym1Rv3DKwhdVn4oSV4nfrjrs1yYgrOU+PTXqhaiPTfkoUNCh+3Bmb+F3iOYcZYXKC2V0aSc4UafwgIroZ8+xYEKTf5YxolraOUgPp5UGuXR+32CH2JhlHolx6DjT0cTlekjghTqDcTe7OggNj6eREqydaV0nHJl0US/nGzvVEidVHHJu43xx5hVxFOq21kym7IiYrYniKLRxZFSskBgzR2uqRfSdZCPNECVtWwyd+tx1Xr5bG8JiwW7ZsGbstXbrU4sZf8wXECy8KKmer7CuB947DbBms6+MIWzt+7eFc5voRefGSThbPxQ4IGNMmntzudEdQYtVaOGUIJMm4K3MEd5CtJAO03Dwn9JqVExtiEgHuq9JK84UbA6TVRhTYz0/sBFPHt7c7ydgqm4EWHQy+t5eZKbYCwou2KGLPeED4iK6Fe4e3gt8nD3Tpe9DaNv69VVavv39tD8n/sy12bBXXdgceL4jW8SWPDrNagEgXU7ZEACYrSYvFSuP1xEkTH4v9cc8Ue3bf/XHvQNke0+JEZ+u4xGSle3+wzK4NDfSHFvFhNve1GPflmXPOPLbHx7aDN6/sZveck1rVzd9Tz2qTSpEuPPk1RDo2TyQs1Qr7BBeJK55wPBfY4vZvrD07U0a1senhEBdf6CqUxk6qHUO44KEh0FSmCoJcXJkUtJZKi/yO65RkyoZGCoVrCIaCiIsMT88F949oDV/e3MfqM+L22VtUXP6xZWa0WDhdE8Ju2LBhdm9a5+s1x6zaeHnCHcsnaSxrwtur2MOWBeQ6GXFwWU/L2KEMo/BbdiAH2j290GJ174mAYL6SQXEgVxgTSRZKMdhyecll1/KG7Rweu4An7vA3l1nEMjiKcXNnhT2mYyLcPLCFbFauOMmIj0UwI1gKWllaN4mwWoXiBWTyD1tMNfqUXgxd3W+42HhiXHtZi5aI3EWaWznkYgD7p8fJLlbQpfuQJD7GE+ccP4e+vKUPtJL8zpzmgoARF0AiUuEjF6/H/9e2E+eg07P/WsS1eeScMx6XV/ZKtdksPlwQsmI4hsgcmazZO4ekW9TVQvCYxBAKFPC8Rp94rfHEcdmzWQzcN6K1bGaqOIHayhqVC83omBwFvZrHWFmQ8IZjw7g0jqM4KXfCA6JCAuC5iZ2gsRuJQ2LdOo60WG6JUbT+vPEEvDDPctG80gMF67mQfPuqbjbrqoqVJ2zFrn683Dq79tp+zUztG0WOnC2BHi8usogn9OQ5h9eMx8a2g2jhGJTzTMXb2Ld4LkmvdzhvOFOWqEEKFBcUFMBbb70Fd9xxB7u98847UFjo+VZBaiC1EHkq/oCvCsNlrAac3+4Z4FLKs9Sczy16crF6hZK4BDVX2PbcqPeOaOVwbHITa7BESPELwZ/bTlllBjvzmzk9NjtZiKKF0lb8ozQmirsmpaUicAEwf9dpC1HHE0fUbi3GV6CO3N+djHX7uqXJFy+2FeAt3Xd8BfvAT+bCs57s28mPFXslKz6+vpdLx6XU6sz3zWO/7bDKQi2QmYzUsvzYOy7FGoTlVfL7qJGN/Sa6y/j4Fu09Y5Wt7plzjh+XtqctnED5dU8szCwidyriV0or++NxslhmbOWeHJuD0kgXd0sxiVtnkF5n+LErF0bhieOS/z9759xLl3Y2PS4TPC6Ojiu5WpM1tXUsDlEaElDggesJ33f+Cq+XA1vFK75e4u+WLOPp8pqw27x5M7Rq1YqJufz8fHbD/rH42tat1itdLWFrMlF7ksEDgk9q9g74Pi3iTCnbtqwHcrE00ng9vtKUm7A9cTLzlYy97Lrm8eGmA92Wm3mAzIoF3ULSYo7oMpGLv/DEJKNkbKJl0dbY5CYpJuwCA6wmUFtWELWtWkrHNmVUW1NDeWcCgaX7DsWCrdhRTyw4+KQRbmcxhcWm+YXY1r6bJLGIy7k2ucVSzt3ribHVKJhkmkQGwyXdU+yOLSUmxOF+48elXAyiM63Y1Bwbcs+wVnbHJndcYuFeaYIWHpfSIrGOMqE9PTbe0SCrQN6laCvZSLrvcB6xFYvnicUUvwaH2znncC7g85itfSdnhZb7zU6eK5c/5zyRbKbAgCEuqGzNR3Ilv3AxaMvC5xVh9/DDD8PEiRMhIyMD5syZw27Hjh2Diy66CKZMmQJaxlYDcrUzEMVyB46yPrnws3XBVKLq+UUqWeairbaww4sGz/qzZz1A+AnojACTXqjQVYkXYjnX38HsYitLg7twd4ejk9nR2ORqieFXSl1kfHxyqO1q5nEojsbG3ZXY7cAZYSfN/D50psRm1vA5B2VwnAUnPr6Kd3jOOdh3cvFp0oK5PIZUzjLricUU7xBhz6ql7Li0nvTlCg5jr065Woo4sUrribnLGmPYgqPrCd9OZydQ6TmH4kfumo9W8myVY1v5tdnROcfdlRgTLWept1WbUGolx2tJpo3MZYyvVBvTOSfTh1eE94y1te/kxKicsMstqZRN4PGExW7jsXxFC+Fw4zlny+Ird71Ene4oFKbBLXZPPvkk6z7BwcdYAgXf8yVhx9OwsQeimo3JVx7KNcVVyJUlkBMytix2ttxxfGWO8DgEOTP3uqN5zI2pFjtPFZou7D1txPpw+ARra2zcRC3GnWBM28Oj2kKkYOnEiVLOXY4B668usIyXdAdc0a42xqE46kjC3UK2CoryTGUxGQRjie4e1tKily4mT4iB9yLPqdyYfJXxuJQmcNhK/MFMOrlSNXxsOGGKsU9oSRYtzFgAd6fQqFza4QMTg9QCi1zj5IfnE1qulAgEW8clv0CLAg9FK1pV+Gs4QeEkKtc+DTPtP1CxfyUGlvN9J5eZJ3vO2bJqGfedWJgaxSm6y0RBjNcd6TmH8yxaYOUSZ9wR5LysjqNm6BHGa4Ktc45fT/jxy8c7oUuyxQLZIOysj2se66omy/aftdomOfA84r+/XF9X0Z0nHgN4HRKf428jLWDMF1xin2E1wMU2LxHj6HrJPRW2jks+zw1oaXZn4lrqyXHt2XWGL6DO2ZgLcI545BfLOF53+d34e9nqD83h+83WdZwnmEiNFt3TYqB1QgT0k8Qme0XYRUVFwYkT1u1tMjMzITLSXKFci0itPmKAtbRnojvwWk+D2zR22PKKTxS24pb4BUi6eHnvmh6w9ZnRpr/FDFPRXSleyNSsjcTHhoH1A2zEFFiNzcZqk6+w+WoOCQ3yg4dGtYHt08eYTii8GNgq2Lt0n7kIrrtg1hhfOKIAs0eMMWlCWluJw8csijh8LTk6FLY8Pdok+CpQINiYqNCCoBYYm8ILBt8g6XcoRbwAybU+42PD+oXSUIOvb+0DKx4fzh6j9UNaLFcU8RuMK2I14Mkm6Gq114ZOyXHJzzlxRY0xUs9c1BH2vTDO9PenC8ptFsn+RJLh5w4njS5xtBryWCxXryd8zFwk8f2Nx8Su58aaQkNQ3ErPuYkO/rcr4P/gNdyeHN/O7md5OzFbHhZuGREX0/gattNa/eQFcGGXZNMxLbVe8fN0m8o1CBcb+19f38/+OYfzBLe2yp1zotVHupj67e4B8KgxaxsXp/mlludct1Rz3J6acbv7jeccijpHSSH8uJTraSuec+KiDOOXJw9vBdufHWMSr2UycwE/ZuUSg9y5XnKBjeLSHryuqS13cFVtrVU5Iv6b/DdlKHx+c2/vC7urr74abr/9dvjll1+YmMPbzz//zJIorr32WtAy0pILGAPGXSyOepo6A/bPRLoKJ5SjA/4DGz338ownqVz2pbjC5lZCDro1eA22jinyQfDujM2RqBPH9vrCA7Kmdn6xChdiJnixYzTD88cofKTtj/jYhsrEILoKupl4L1O5OA65WnaY9CBXQ8m0ShO+h7+GY+PiAy12UlfsfcbEE+xrqhZn0YVRWcP+d790+/tOXIygJUwKHwdOoOGS3wn/lvelxPACqWWkXVIEtGwcrv45ZwyEF9tfOTouX/5nn2zsEp8YxXqFHPz9uLUWrWjSGMKnJnQw9f1VC97tob+Sc854PftqTYbsJM73nSjIuTvP4risroXNGZaL3av7GGKJHFlEnYEfX7hQdGSx49dADAWRK2/BrydBQsF0/hqOjVuuUPRukoztwQvaqH49QXHA41QHtXacAcmv9TtkrNzmsflZiHLefo3Ha6HokVqRxTGp6Wre58Q5JxYplou75eFLcqWz2HEZYD4updckXHAh7RLVMyxhWSTcTJxjbWX7SmvZ4d/IZVZzoS7nvcN950y/c48JuzfffBMuv/xyuOmmm6BFixbsdsstt8AVV1zBulJoGWk9OGyHclG3ZNUnGS5C0NTqCL5yxN6Nchdi3oZFzh8vxv0sMa4MxYwifgGWa43SEGMTtw9LsUiRsyqkCaVh+AoHK+lLrwWJxnIqSiu7K4G7FVJtlPkQEYX2u4sO2b4QC7+BWGqDuxYwe1oaBpBi/P9q9jHOLTYcR2gFdRTILXLb15vsWkbkYmvEBccuSXFqjFcZ3SnRA4spw2/Y3sFFmG2D8YdFd6pcGylu+bZVMoSLInQnS+ElEdTszMktVGIJIVuI7mPsw2xr34lW2fR4g9AWj8s/t5+ySljiLmxpvKEaY5Ob0KXEhZuvgVNn77R5PREn0FZNwq0ym+ftOm2VPMEtdmp2RBGLAotWNlvwfz1NJqPVNDZ/P9lOP/FG7wbuM6nwwd8DSxyp7QXg55wj4SM9LsVWgxxuhRP7v4rnH58Llh84a3VccqFrq3ajO8clzjOOrpdiT/abvtxgV5RLt9lZPCbsgoKC4L333oNz587B9u3b2Q0zYzFLNjjYs015P/roIyYkQ0JCoF+/frBx40an/j5b0mYHA1rNFjt1TmhcEWEALB4LXVMdW1zEeArRNYS97ya8t8pUoR9XJUlRIfCscXXC1T7ffukE5eeBsaHVjReW7aEgLV+8wIoBr2jhuvGLDfDFaoOLuH/LeFYgFbOLxFpB/AIm17mCr77VFAe8DlZTB/EwUmEn7kP8jR76eRv8749dJnfzzQOaQ+emUfA/ozUH4ZaRpftzrIpIx4cHu903UsrZEsP/cLaOljSpB8tEXPXJOtMk8dzFndgC4vUrulrsdx4sfijHMnkCd5vax6VoseugwHpgOambL9o5xRVw5ay1puPtrqEtmSUJi5OK8IvyIZnEEE+MjZ87vOG4PUTRJRYJx/Pkrm83sxZ/PAwFs4PHdkqEFkYLqnhc7sgstN3PVMVzjtddUzLRiVX+pXFkz/61G+78drPJHYlxuhi/NPMGc3mbQOP1aI9MEh0XfWpeT7g4wHhhR+VOHAXxj3hzOXuMVnd0T2Kozf8mtLcSF2LcGwcFBc4dSHZRufrnXHKkU10cxDMD4x1v/nIjLDGKPSxlM7h1Y+ZNa9k4wmou2J3VMPuOh8eIYUK2iBKMLtKSXG//dwAmGYsTnymsZEXvcYE/517XisO7JgedICwsDLp06cL6w/7333/Qrl076NDBPHGpDbp+H3nkEZg1axYTde+++y6MHTsWDhw4wFqbKSG/rBoaBQVarNz5QaFWLzfemxUvKo7ceQiPL5FWKX/41x0WRWr7psfB+v+NtPp7XMnghVZ6QBnGZnQ9qHTAZxWWswsLXuCVmL3F2l+iyPts5VFTMDi38Cx/3LoiO7ceyJXdMMVsqHgy8//jKNAZiRWsB2IjbOxi8td2c49VHOd3t/ez+nt+ofpPxurDrQdqCjtusXPXjXaHcfLkog/d1pueGmXxGXQtoFULJ1ipKxYtdmqfc5jgwS0RbRUIO1GIixaa1xYcsHDRtUuKhDVTL7BpkZQLwA/0gPhBwYkoyaITrQLiOYe1Ev/be8Zi3/3z4BCrv+cuL7mm6kEBZlemN8bGY+wQMXwBF4rfCq240B2Gcbp4kxOmclb+QA8Ich7kHyNcK1yBL6Q4KMTXTRspu9DEa5i0TzATdkaLaHahet01uNuxdYLjc07cJrEOK+63FQfNhZPDgwLg+zv62ZwLMiXzHKL2PIfw8BolCw57Fr33hRAr3D4seo83V/GYxe6qq66CDz/8kD0uLy+H3r17s9e6du0Ks2fP9tS/ZbXy7rzzTrj11luhY8eOTOChuPzyyy8Vfwdew1PE4rIs7kJdgcDTuWNC7WfScMQsQn7BQZestOWSLZEoZ5bnBxuPNRGbQasxNrQcKFmBiu6VEOPJjHEniyUJD7YKO9rLKDZNoDaCcV2BW5ek3SHkEOOvGhsvqigSpPEx0vZvVq5YmRR5Mc5JzRg7pImTFjvRwift8yi6TaSIcYeiaxZ3m9rnHK/9heLAVlcCW/UT+TmHYuW/vZYiGxNd5LBXm9ITluTtxoB+JTGX3I0viiW0IosLKWR0R4M7XEqwneOSX2vkyoq4yjYnxiZOoG0TzefoFkm8HK8J56gcj5xoVdViZyzpI1oanUVpGzBu5efiVPQW4bzHLXZqtd7Cax3PcI0KdSx+xBZ4/JzDWLvlkhCdLja8XLbmOU8t8nnJImf3HVbC4EhDbIa0cb7TRIMJu5UrV8KQIYaV3h9//MF2MHaieP/99+Gll17yyP+sqqqCLVu2wKhRZsuAn58fe75uneVqBqmsrGSWRPEmDQDmVi1zto7rBwX+Brz4Ixc/XMg44oPrzP01Zy4/zJp3t39mocVnruptXTBVzq0kxnCJwcLuHvCFZZZjkytoKsd1fc2/9aZj+TBrxRFo/dQCizpY3VKjYaCNwOJymewwjlpJL3xs6BLgFjslVh8UtrzlFq7E0Ap50Qer4ek/d1t87sYB8qsz6UpQLEESY5yQ5SxCzoDHJE9a4dmpjRVa7C7r0ZTdowsZj8u3/jsAY9+17MP52U22s7nEUCWx4K9hweH+vmPnnPH34RY4pZXcp19sDmfA/pRoNW379AKLcAFccNmK2REzfcU4IHbOqTTJ8LHh+c1jg5WEP4zqkGCRDITnXMv/zTeVbkDwuLWVXWvPQsHfw2Bwd8aHY8P9x2piGtuV9XRQxoUzqLVhEZgQFcLG9uBP2+BWSRyoGPIgYi9bOsjfXxVrJJ5z3ArMa6uJlkZ7PDiyjcU59926DBjy+jKLz3xu45yTiqtRHczCHfcVv2a7YyUXzzn8Hn6OK5kPMKyB883aDBYT3up/8y0y4zFWz5XaboF8LnBzkS8el9yNrnTfYas/BD0YuO8w5GHC+5Zlgd66yroHsmZcsdg6LC7OUHdl4cKFMGnSJGY5u/DCC+Hxxx/3yP/Mzc2F2tpaSEy0XGXi8/37DTEjIjNmzIDnn39e9rvElYwhDs198YMtk+btPM1ixH7cYCgFE6IwkBMtDGiZwhMFM9nwJoVnGToCM6+O552QmUBdP+CxHtdbiw7C1b3T4JfNmbJp27bA3xfjeNA9OXP5EdnP2HNXHzC6teVQYwJduPs03PP9VlbG4W9jLS20pCmNQ8PMx1Pby+GnjYbfxRmwLIcIxpNwNwMPhEZ3GZadkCsg6wgMoB719gomUFD4YG01Zyx2PHMVg5XxJoet1k5W3yUEsGMJAzXOOez3jDGa1/RJg583ZVr8bo7ACR7d7Sh8/th2it2k2JtgxI4gGHLBrU5soajCJPPLphPw5OxdcHnPpjBnq2HbEqOCFU0y6AYf3q4J22eYdGSvor4c2Pt5wW6z5RKTbXgfWVHEogi21SfZHpsz8uGKWeuYxXDD0TxTgoFogbNHh6QoWHM4jy2A8eaMa0xaaw1/0zNFBpGuxiJ4y/FzLJ7q8h5N2SKR99gVg+vtwb1Ju08VsZvsGITFu4g0sxLFIQfFqhrXyyd+38lq4T19YQeLfuuOygtx8YUJd5h8h/F0PKZOJNqO5Y9XLJBDjYUiJnTgAgGrLWCiHz/HlSS9IOnGaxxaxqXWcY6S0CyvWezS0tKYlay0tJQJuzFjxrDXMZkCkxq0wLRp05gA5TcsycLpJBzwGOCtRkwMijqEizrEmcnY0SrKVnaelIu6GjJ8zRY798eGog7hos4Zix2Cos4e9roriPWcxBUfooY4eOoPg3WNizrp/3SEXC9DpYjFndFVWSeYuNAywgUCL4HgLLjaRzB+hYs6Zyx2YtygLZRe9DA+VPacc8N6wBNvuKgT48OUYG+icHTOiQkll0uskWq4mVHUIVzUKZ08lTZE52JGDt5uDcHaYWIvZLFfq7R0lFLeXWzIIMc+tGLWqNLxKTkubSEmiaDrVzx/A9VYBC89ZKqnxkWdM5ZkJdnqiQ5KwnDEBvNM2KlwXPICx6KoE89nVzs/Oeq7LXVJXy/0REbUmOeem2soBo+LIXHhpnTx4qizCBLmxDnc4MIO24Zdf/31kJqaCikpKTB8+HCTixaTKTxB48aNwd/fH86csSzpgc+TkpKsPo/ZuVhIWbzJrcTR9MtPaDVjtZydZBxhz88v+u1xbDx2a0jrxh7JFkIcddNwBntthB4bYyi6yS/8PBYP780ns+v7zd3gfTHr0FnE2k/YSxH7BnPLAa6++QXFVmFmR9iqjaTUYqfkQmWv/pKYpCFamnq3iFNl38mhZrkDsbC0lJcv62yxyOHWJsww9UQgN/s+J45VWz1+lSDWysPrzkija5cnFPEMQLnajUqwFZ+n5HhzdzHQWajnidbdEe0TTMJLjdAOXiNQSrKC8klKWqopjWeTCmVMAnJ3IWzrd3dmweGoNJU9T8mjkrlglNHV3LNZjCrWVluhWEpdsfZEqekzTpSZanBX7L333suyUrH7xOjRo1msG9KyZUuPxdhhiZVevXrBkiVL4NJLL2Wv1dXVsef333+/U9+FQZjzHhjMAsGxcCO3ZqgtflxxnylJsJDywbU9oPsLiwz/M9AfFj08jFlpruydCuuO5HlkbK6KDTlem2QukyHlvhGt4c3/DprG9tF1PWHuziy4uGsKq/vn7oXe3SBwW+2yOO9e3d3me2LyCVpBsNMFijm+r3HiwTIoco3YlWDrOtMkUtmFytEhwyvd22LWDT1h0sfrTAuOxY8MY2Ubru6TBv/sOq1qUo8nhN3YTtYLRjF2lFt78bjELL6Fu7NZXCJf7at9zqlZf+zj63vafM+iI0WQPzx9YUfomBwFozsmmUJHcFvkWqm5s5hSWqTVUZ/a54T4SXvXZLSSP3VhB7bAGtUx0TQet4SdjeuJmLDnjjjApBB7vxOGPIjW2gUPDWF1JNHt/YvRsu2qAcNW/1k1F/k4Z9lijHA+hgb6w1tXdoO/dpxi3UR4wWN3rK3VNkSnUq+EaOWTY4okQ1tzFjsERdZll10GERHmuAiMsRs0aJDH/ieWOvnss8/gm2++gX379sHkyZOZOxizZJ0FM3QmGYMdPZFR4+4Bj8HNONHjQbXqiREWLgR7GXoYUIxxT9geCAWsGvE+cmQ6cGM54s0ru7EJ5Lvb+1q4DKSIF7H+LeNY65abBrRg956yRjpDU6GYMueTG3uxsaFV51JjAoKjODYMZMf9hfuNx61xi520GKdSbK2km0QodQtZv4ZdFXC77hicDg8YA71tgVZIUbhiLBrGoLLYTw3sOzlwfJjVhgs/e11jxOMSXZfYMQGPS4yFVSOu1V3EzDzOFzf3Zvvh/Wt7wHhjay1b8MkMLZB4fcEEIJ7hzi1Gcj2EGwI57wUKVXSdPzK6LdwySD4jlsPj3VC4Y8wTjg2zn8WuFK5ia4/byq5W4op94ILWbD64tHuKqcOCLTC2D+lj7HqCHqmr+qSx4zXAzXPOVoN7adccZ3njiq5s3317W18Y0kZZ14/BbRqzeqd4zmHHDT4XoMCT62qhhEYO2oU5gnvKRFB84vGGcXtTRtlfCGuijt3Jkyfh77//ZlY7zFiVliXxVCuzs2fPwrPPPgvZ2dnQvXt3FuMnTaiwx/yHBlu9xk3UatZmQsSYKUfcOqiFRdJEt7RomDa+A0wd197hShYP6vkPDmH/T5rRZnIzqzyBOpO59P3t/eCGLyyrcV/RK5VdhJSYplHY4mqxhxCTplZNLcNv6/oE/M7V3WDcu5aZTzhhjJ6eqGhsv08eCNszz8GwttZ1GM0FR11z99qKg1TqyrmiVxq8Mt8yMWlg63hmNVAyNnSr/HnfILYd0mPYtO9UPi6dKQ+DTe/FDOb0xuFw59CWcMcQ+1YRztJHhzHLtXTRpUb8oLt8c1tfuGymoSgqZ2SHRNYLVsm++3fKUNhzugiGy3gKeDkZXgXAWZxpnyQHZryKyR0IClU875SMbcGUISzuVzo2NeK0bFnclBQ8l2ayinGOWGxZyc9219BWLPmlb0vrpvLuuittCSZnrOR4XGIxYpEre6ex+UDJcbFm6gVw7GwpK2gvN8/x884Vb5mtUADe4cgRdw9rBZ+tsuzJfkn3FGbFV8MF63Fhh+7PiRMnMtcrZqR27twZMjIyWJpwz562TfxqgG5XZ12vIs3irC1f7p7Qci1oMPvH0cpRBEWcKOxuMDaMVnoRlGZYcrjQE8s4qMFXt/RR/FlcXYlgRhWi9GBHC5Zc9iUXl7YagitBbhNmCZXqHYEXUZE2CRFOjQ2tXxe0T7RrieUlZpxFbvWPleqVHlO4bdhx4cNl5gKb6JJzZmK21XbOE+IHrRqPjLbfRF4EraOisEPLCKJ0fC2bREDLJrbPOazxhZOhM+3b7IEWDaVIF0G8rpvS4xIt/3iTg5dxcrXGotwmvHKZ8thsvBbgeSYmBDk1tsgQSGhnPTbe8QaTp1zNRJfbhHuGtVK8EEYrO3YmmP63IZAfwS4MSseGIgvdyrLvuWmxq5WZ5/DYRguwqyFFj49t59Q51zQm1FRiSgQXj/gTofYsrqx2TdjJuCjw+if3/2wtZNHzMldIxHOn20iDu2Ix4/Sxxx6DXbt2sSxYLEqMWafDhg2DK6+8EnwNd116coIQLRVKDwi5VY+tum7Owt15KH7U6oGIbg+s1eMqtzkheO3BV1IoWsuMhTLdXWFj3Ni4zrZjqxzxyuVdNHNc8vp14uoRV/SubAOfYNy1tki/V01XLFp2MUjcVXjdPncx9xx13aol5YVLOrnVnH7aeHPrKXdxt2Wa9Jy7aUBz5qJ3BnEx96pK5xy2/eKFtF0t4is9PzDJa6qTv73U0q6WOHA3YUl6PUE2/m8kjGinrOuTHJOHOXc9sgUKTJ7kwItCu2uxu7BrMjxmFJ5KwVqojopka1bYYXzbTTfdxB4HBASw7hMYa/fCCy/Aa6+9Br6Gu61kKqrUdbkoadXl7CSDlgOxtIB73+l6FXVELbM0xjPx0gvYn1eNkznMxcbMHCXNsJXibqyWdIXtTIkaTkml+SL53ET78T3O4In2Te4eV2qKVh7jplaSkbvnnJqWA3f7xVqdcy7U9hLreg53Q1hI9z9fLEp7NytF2tnClUbv4nFsrwC4s3B3JXb+UcsVq5W5QIwLdfWck1rWxbZnrnwHJon5lLALDw83xdUlJyfDkSNHLAoJ+xo8yUGp9UBq+ZI2SXeXCQ4Cm50BA/L5xeWcggMex+bIsmer5UtDCx8k0RjQba8ul4h0bGL7JbHjg6u4ciG3hbPB3NKxSVfYzpQl4IgWJyX9ID15zonjc3VysgUmCaiJaClX45zrbieRo6EJdDK21eE5pzDrUEnbQnfBgsXOWOykY5MmSWBgv7OISSkjjeVY1MDZGDvp2Gy5Yl1F7JLU0Oec3PikY3FXtLZV0UDTIMKuf//+sHr1avZ4woQJ8Oijj8LLL78Mt912G3vP13Am3gdPusGvLYMnft/hMWGnNrxZvaPsSjzQr5y1jjWctjfRqCle3IUX61RyIX7y951s34lZXNJJhv9WWoC3OFJyIcbWSj1fXMS6Tdi6ECvtFiKilivRnXMOxz/+vVVw+zebfeicM2Y0KyhVM/n7rTD6nZV2S++I7ea8jTNu9NcX7oc+Ly+2bAAf7O9SOYmGgPdTVeIBePPfA2xsvJ2dtCcy0kRhJxRb55yaFi1nrOTYEaTr8//BbKENnZ1mJZogNkx5FYGn/9wFA19damqPJmexd3fB4Sk8Juww6xXr2CHYtmvkyJHwyy+/QIsWLeCLL74AX4O7vJRMMn9uz4JTBeXw6+aTDtPAnYVX57+0h3wPR3cP+AIHKxk8IbBa+qaMc6YWQmqBcTTIE07GLChdYecUO74QY+cM3Hd/bT9lM94nOtT5CzEvVqtmHJNoGVEygb66YD/rK/u8sXo6Iv0zV1yxmOklllHwxjm3I7MA9mcXw1KhBZFawg5bySHOxh6qdc4hC/dkM0GONf7UdBPzwPTXJqlbNN6ZIHxsI4jXkg+XmhNwpH/myjnHe8GqFa/L4QkjSgqPY1IRju39JYZuE3LuSqVdXuRiPTGm1VuLqUd+3cFilx/9bYddi50rYKkke/183T7nSh2fc9+vP8FqMf68ydwpShqtEOPCcYmJMoitPsxq4DGzCmbDim7ZWbNmgS/DLVC2YtBQNKAbC9P85VxAak0yP93ZH0oqakzZWWrBXXByhUGxejxWS8d+kGJ7HbFUC1Zld7c4KmZ6YR0fV3pL2oPHxMm1AcOxYeYedloQJ0bx4istSePKKu36fs1hfOdk1ccW5OBCjC12MCZITLwRx1YrWWK74orFtmdbnxmtulWFn3MlNjJH0WKCta0wM1isVo/nH8aLqRXX+t413dmxqbRWlVLsNVznIRF4rInHpTjOHs1iTP1nXQWLe1/bt5n6x6Wd2E8Ue6fOlTM3m61zTnpcunLOYcFdTxyXYXYyfnEBX1BexbwEoiVN3G9Wws4FVyzWf9z+7GjF/cHVcsXmllSa4kPlrPvS/eYqWBT63hGtVT8uQ4Nsn3N4DcV5HBMabZ1z+J7Yn9eV4xJL02x7ZrRHrX0e9ZcVFBTA77//zuLrHn/8cYiLi4OtW7eymnJNm6q7uvc0XEgVlhsyR8Udj6bavi8vYY8xc4sXlBVxNe1fCk5uaos6Ryvs3i8tZgc9xr59f3tf2QNeSasUR4gtstQk0HiBlRtb/1eWsFIh2O4J63JxamptX4jttW6zh0fGZsd1suZwLlz/uaE24LLHDC39pIHD0p8kxMWC2Z4YGy//gLoawxvEeBZ02w2YsdTUH1gskVBlFHZqLabwuFRb1NmbRPF46/HiIlPdvP8eNh+XtcJ+drHGaoMel3LJE1img/fL3vjUSNPr4jEs/TNtnnPWY7v4w9XMsoqXnP0vjje9Ln5WDWGnRnyXs/MAZnPiXIBc3rOpbHkWtcJaPTYX+NueC276cgOsP2qwiO96ztDbXhqHLP0zV8WZJ64nDeKK3blzJ7Rt25ZlwL755ptM5CFz5sxhpVB8DR4wjxcf6YTB21YheMEST1weh6GWK9ZT8P6DUoGAIpZbg7BNT2mleRxiLR5nCi03NLbED46N1387eKYESoV99OI/e22OTa5iv7ewN4He/+NW0+MZ880NudFlaWtsamV9qmX14VYtaRzfTxsNrY+QT1cetTjnuBVL6zF2to5LMb7zWG6pRXusT1YesVtaQivYc+lxUYd8t+646fHsrSdVtZJ7Ci5+xMUfh8ev4q7ZIbQS/Gt7lk13JXpCtIK9haIY5jBn6ymLJLITxlZZrnZ0aCgC7IyPizpELG791iJDu0rZ49IFV2xD4OfJ1l633HILHDp0iNWx42AixcqVK8HXQPM7T8GXTjLvLjbveOmJe8e3m3xskrG8EP8tiDdeUFWM2eJo+YTmKfzSsUkr01cK+0isLyYdmycKSrqKvVZ3GE/HOZpr7g3JY9LkxnZWQdxQQ8KtAtJzToxZko6fWym1vpiydVx+sdqyMr1oDcfYVh7qoelzzoZlRCr0pA3fM4zHqXRsznSxaahFsHQxtSfLvMCX1nfkIl1OkLsSY+cp7HUheuCnbTb3yeUfr9X8At/ePJcjSawTQ47EOFgr742GEulEPDZDbdq0Ce6++26r19EFi62+fA20ZPADuUCYMBFMJhARj23uj5cG2sq5a72JLRP8BkmwtlhckYMTqJJAYq2dzNJAdKn4xvg0vAhvN4ogX5pApRnLPIFEDMbHz4jWZq1ZRsTtkZ5zUuQWTtJaVRoyRtoNEZi3M8tuGEdFTR0Td3sdNLrX4oJDup94hilnY0Y+Oy53CtYuV2M/G/p6cuSs5eJJKgLWH80zjq3QquixFo9JR+V1RGGHsXdq1mT0FEE2rpfS+UualX3yXDmbCzC8RasLDhGPHVHBwcFQVGR94Tl48CA0aeJ6dXRvgrFtmBUqWg+Udmp4cZ7BtYfnDRYl5JkxmluFSlbUeECLFMsIu4kfGsraINf2TWN9/XxhApWOLTO/3OoC/sHSwyZ3LcbhOdOOqiGwlTxx1nihFScZtDrzseDKeuWhXJNoHdUhgdX6wiQPLRFlw2InggkUcta5+wRXNB6XN/ZvAVrClhv9qEQgSM853JdP/L7T9Bwbv1/eMxV84biUlgiRvo9/99vmk5BhdO1hCZcHL2gDWsJWV418yTl38pxhDOL+nr31lMl6joH4D41qo6nwB35M4rSGCQZcUMt5BOQyYHn7PTwnMetTrU4tahFg45wrklxfpPsWf4dZK4+YLMxX906D9smRLhXO9mmLHfaJxS4T1dWGHwwP3hMnTsCTTz4JkyZNAl+ExxT8sdVcCuPrteberZz/9mRbWX44eFzMuLwry2rSEngiIt8KMS94EV558KzF56TPf9p4wqIfI44NsyS1ODaMy+ITCda0W7zvjMXnvlh91OL5zOWH4R3Bzf76Fd3caiXmSeGDLjo+aeLKkifzcDBjWewn+8mKo/DdOvOxi83RX7q0i0v9Ez0JZisj3683H5fzd522+AyWXNh6wtJqvj/bclGJx6WtXsnegmc04r7giDUGRUuPtB7hnG3ma9C71/Rwq5WYJ8e2eF+OqZguiu+x71qG4fy1wzwO5O1FB+Gj5eayJ9Mv6qS5hSK/nmDMGWbVc6vqc3PNcblyLvW3/jvArimc6Rd3hKs0NrawYH9TYfDpf5nLIk3+fovVZ5ftt5wLDucUW5yT2Nu3TwtDeS6t7bs5whyOxpnrjOEb0lAVsR7h6wsPWJSvulXlMjo+IezeeustKCkpgYSEBNZODHvEtmrVirUVw0LFvshWY1A21jrjPC85mZEdElP76HdWgNYpN5aGOJFfZnIhrDpkeeIiX62xFLLT5uwCrdMqIcL0+Ou1hovt2iPW3U9wEhIRA555SRetganznCtmrbXplsT9am+8WiooLXLkbIlVSIBYh08umQIZ9+4q0DpxQnwOFwhS0SoVfsjHy80JFFqlVUK4xaRo6xgUS0fwzxw3WuvU7hjhiesJFleWs/4jUpcrLq5Ea6wWx4ZdiHgpEHGek14bEaz3KTLq7ZWadC+LYJY55+CZYpulTz6XiHIMXdFqnLUcHtu66OhoWLRoEcydOxfef/99uP/++2HhwoUscQLr2vk6UkVvD7F+WguVW6SohVh/iBcK1XgcrGLEoruvzDdciF0pt5SgoSBnudgjPrmICS4cR/tSq7ta7BbCrcVKW8NpHXFC+Z9xgaTlhAhnwHqenG+MXgBXAutbNtHeXCHGVWERW1fH1qqJWSBqlU0ZtgtiK0nC0Br1wm7iVkjRk6EXVP/1161bB/PmzTM9Hzx4MBNyM2fOhGuvvRbuuusuqKz0zQuz2DXgtq8N2a7O0kJjSROc+4U4Fu5+FGMolDQ7dqcnoCdpl2Tdj08cm9LetFqKhbEFtpxyJRtU2nRdK7x9VXfT45u+3OjSd6TGaqfVlsgl3c3xR/N2nraKZerfUltuLGdoIrMIUto3VkSLMUzxMjXIXBkbFtbWIm9c0dX0+FnBHeuqZUxL9GgWY5XsUiazEPZ1VBd2GFe3Z4/5YNi1axfceeedMHr0aJg6dSqz4M2YMQN8kTuHmLtpyPWamzzccULEjMvVbd2jFq0F9wJH7KAxY5L5ZLfFH/cOBC2C8T7SYpeiZURJO6VPbuwFWuWlSw3tynhWmlhrUOkkfIGKjcTVZISD7XrwgtYOv+OrW/qAr4gfnl0o3a+2+OEOQ9tGrYFB+BO6WMajipaRZy/q6JTA0BLohsOEFVvVAj68rofD73hdwfXUW0wUxiaXHHhR12SH3/Hu1eYFmZYICwpgHU9sHZdKkho/vr4nnHfCbvv27awvLOfnn3+Gvn37wmeffcZq26Fb9tdffwVfBFvEdEszKP5LuqdYZOrhRcyRpWTKqDaQHK1N6wGv4M8nHDyhnxFWa46sHjjBdk01r4a0xltXdrN8/p85KaJNgrVFT+SKXqksuUCrXNnbnBGJDeVF98mjo9s6/Pu/7huk6ZgRrHKP4LknWrQwrEFOHIlc368ZtEm0v3+9CQaYi4j9pXlijC1GtGsCg1TuFaomj40xZ5Dj9eSDpebag46yJbGTiNaSJkQeFs4rHBv2hOUMaWM/kWVIm8ZwVR/tjg3j7PhCuHPTaIt5DbPnHZUeQnGUFqfNkCM548orQvF23q/cFp2bRsH4Lo6FrbdR/Wp+7tw51jKMs2LFChg/3txapU+fPpCZaRno7EuM7ZRoSnkXM/XeurI7jHeQManVAHVOD6NoxQlT7PuKnRY6OnBXatWtwMGyCWJdNNEy4igTVIzR0+qFmO8fHBe2bOI8MLKNw7FJa4lpjf4t49k99vwUaw9+e1s/GN3Rt8+5NokRJteV6M67oX8zaBwe7HNuSpF4YfuxTMTaI3mKWypp/ZwTtx9LZ6w6lKu4tpnWx8Z7CCN4TP4tZC7jPDeyg30reoSkBpzWSDEaV/i1YfkBc5JgSox9A0ZYoLbPOY8JOxR1x44ZMkqqqqpYb9j+/fub3i8uLobAQG0W9VM6ifLAZ14cFgkJ9JN1Z/rShZgXFcWTmWfp8VggRwVCtS7sgvyN+626zsLqg1YPpU2/tUy8sS0RWuykPDzKttUOBYXYrFyL8PILuO+kpQukhZd97pwT6r3xsiDIiHYJDveLlor22rueIKJo5S200Prhq+cc32/SJBgu6rhnxxfHZnHO1dRaxBZjORRHJVo0PxcEmM85sQuIkgWu1spB2UL1PYAtwzCWDnvE/vnnnxAWFgZDhgyx6CGLZU98FX7AY9X3BbtPmyxaePA7mkSk1ay1esBjFe4pP2+3cCE7QuuWERTevBSIWKLlNWMcDyZ+2MpI9IWTmbtOXv/X3ObtvWu6W9RusmfJ9IXF1PG8Unj01x1ONdL2lXMOF1KP/WYem5KYR60LBFHYie0HP7upt81eq75yzuE8gHoHQ9DeEOqbfXmLYWzVdpIpQjW+2BDnuX/3nIF1RksrGjIwdlLabkuKNJ5Zs8Kutg6e/dtQUBn56tY+Pn/Oecxi9+KLL0JAQACrW4dxdXgLCjLv6C+//BLGjBkDvgo/4LGQKK9Ozd1Bji5GWhc/fBWKbljeKB5XnvHGIrEj7Uw2Wj/gecFU5PctJ037IyHSsEp7+yrLGDxfGpvo3hFLgfRNj7OKwZMSEax963mwUZRnFVZAtrH8iViQ115Gr+bPOeP1BAu6LjO6hLAjAbeSPD62nc8el7hY4r//d0LYSvskg6VuqlBlwNfGhvtHr2NDggVrcFGFITGEd25xZElWWmVACwuO743lanDua2+snsAXxL644PCYsGvcuDGrVYexdni77LLLLN7/7bffYPr06eCriAc8Jyo0QDZj5oubDas3n3ELydQeQmsk5xUh6FSaAesrFjsR0ZIllp7gq25fiomR23fcLSSK2qcv7MDa2nHqNVvBznoxZeu4/OPeQabHP99lDvtAwjR+XIouPbnjUszSk47NFyYZOYspPxeHt0uwmQGr5WQee9c8LtrEhYc0A1arpYUcnXOdhM4tlxuTXwa1jodnJBnOWuuDruScizB63aRzwawbevmcKEcCPFmgWI64ON+tzYSEyBzwPBgTwZZTqPjxJGgtybb0FRO1iJ9gdk+MCmHmapxUe0jahuGJoWXkatCJCSI8OxTd0Be0T2RZz7zzxFmZuDWtISYVyAnSZY8Nh20nzsGl3ZuyizbPeMYxirXitIhcLJkYD9MlNZpdgNHShY9F4sKCfG4CFTuHoNXr17sHsFgnnkTCCdf4QtFWMWnxXPx3ylA4cKYYJnZLYR0neHap3PGsNaTXD+nYFj08lIXs4NhOFpTD+0sMWcHrJC3ifOWcayaUCXnukk7MIzC+czLroc57ofuCKJcTdlgmSmTu/YMhq7CcVUNAIc57xPJYba2j/SuDE7Ro0QKOHzebxRGsmYcxf5602IkFcPHEFhW/SBsHyRVaPOC3HLfswYlB3XLEanwCVYIY8CzWNvKFVZpcGzFxksEkCV40VLTgad92IC9+pO2YbPXw7d1CW32LlSymxJZaoktdih4q5uO1k18/RUOWL5xzjsAyO7zUjq+NTe6cE1/DziLX9G0GvoifAospLhD5IrFxRLApBCS7yLp1nBbRlbDjBZKxIDInMjLS4we80pgCrWcfyk0yjur6iNY8X8NeRiU29eZc6AN1i5xxhYuuPnsxXFpLnhAZ0MrSeqWHzFGlNd44FyooFOtLVAgJB0oStnwJMXPWXpa6VpCb53zxGu9KRwop4rR926B08AV0J+xQyCUlJTXYAY9Vxh0VSUWu7avdgpS20tSxfMv9Cir7o7tIboLSOvMeMGdr27OGaLnYpq19h65XW4gWO0c1qbSA9JxDMdopRT7UQ6SrxC3rC6IV6yw+d3EnRX/rqLySFln95Aib74mtnXo1972QnVVP2B6bWOS3n8SlrkUC/CzPuZnX91Qk7KTdRnyFTxR2FurdwjeOS9+bjR3w6quvQnx8PPTo0QPeeOMNqKmx3QcOe9YWFRVZ3BwhFTCjOpiLMdtH29Y6uR6I2HFBScKHo4KcWgRj6OwJcl9zc0UKwg5dB/Z6NYoWO+kFXMtZseK+U4IYH6pVpP2VJ/VMZTFLemRgq3hIjQ3TzTknHl7Y19feAtDX+pFKTx0xGcTu3/nAPCcFrye8OoIc2k8v07nF7sEHH4SePXuyBI21a9fCtGnT4PTp0/D222/Lfh7j755//nmn/oe01pnWXT3uJBgodUH63qnsuBhluY9diEU3f7SQpe1Q2AlFtn3FqoVJEnpFy63rXF1wFBv7qDqy+Dhqyag1MK6YB903sSMMfFG0ShdFWq964A4jFRtnfAfNL9cx8QEFh73b/v2G4pfYi3b48OHQtWtXuOeee+Ctt96CDz74gFnm5EDhV1hYaLopaXXmi9YpV1HqgvQBwwijmTCeVAdj87ULsRgjUiHp0GDPFSvT41vzpWrkMpx9+bj0pQQrZxkjCNUEByErvnbOjeloFgRNjLU+9SJaXa7g4CPnXHsh4bGD8FgvaF7YPfroo7Bv3z67t5YtDc3rpfTr14+5YjMyMmTfDw4OhqioKIubI5rHu1ajp4/Gs/M4dw2V/y3laGvsc2krI1FriDWJUmPtW334mMQLgJa5Y3BLxW4fcfXtCytxtNiJotwR2FMWGd5W+/GDyKwbeir2AGATdmdcY95m+kRzjTNHsciDWzdm9+E+kDWKPH2R8rHxZB+5eppaRJp1rhRpSR6tMlOoNyuXnCVnRbcX3qI1NH9Vb9KkCbu5wvbt28HPzw8SEtS9wOMFaPVhc9Nneyx/bDhszyxgtYx8AWcSBX68sz8s3Z8DF3dN8bmLlSN3HlaO79w0WlFrJy0gxn46snxgXNfv9wxgJVKUtOXSAii0P115VNFn5z80BNYczvOZc05048llI4q8fXV3WLg722dctlgWQ4z9tMctg1qw41FpxrO3ERdFjoTdzQNbMNdtfx8ZG3JxtxSYu8NQy1NJ4simjHybpb60RhNhfzmy7ONcgHVphynoK64VNC/slLJu3TrYsGEDjBgxgmXG4vOHH34YbrjhBoiNVddaNrZzEhN2KQpWNS0ah7Obr9A91XbatxS8UDtqCK0lxPpRjoQdJo340tgQFKEotK9VUF/KV7K7ODjZKxV2ydGhLPHHV0gTrMeOSiKhUPK141JJSQkE+5D60n4T6dU81uHYJvnY2C5o34QJOyXhR2gQ8IXqAXKWccxEd/TZK33snGtUX+8LUTaO2bp1K9x7770s3g5j6tLT0+HGG29kcXfoclUCZsVixwyMt7PnlsUEiuUHclhBW0erUF9k7eFcaBob6rLbWcvsPFnAAoPRGqc3SiprYM3hXBjWtomuknoQvEytOHgW2iZGQooOkyewEDgmteD49MahM8VQUF4NfXxsMaGEwznFkF9abbOItC9Th/PcwRx2rbSXNeqr7M0qguraOovC9FpGqT7RlbBr6B+OIAiCIAhCa/rENyI5CYIgCIIgiPMnxk4NuPFSSaFigiAIgiCIhoDrEiVOVhJ2AsXFxew+Lc23AiUJgiAIgtA/qFPQJWsPirETqKurg6ysLJZVq7QIqi+pfRSsWIRZj/GDeh4fjc030fPY9D4+Gptvouex1dfXM1GXkpLCyrjZgyx2Avhjpab6Vkq6sygtxOyr6Hl8NDbfRM9j0/v4aGy+SZROx+bIUseh5AmCIAiCIAidQMKOIAiCIAhCJ5CwO0/AIs3Tp09XXKzZ19Dz+Ghsvomex6b38dHYfBM9j80ZKHmCIAiCIAhCJ5DFjiAIgiAIQieQsCMIgiAIgtAJJOwIgiAIgiB0Agk7giAIgiAInUDCjiAIgiAIQieQsCMIgiAIgtAJJOwIgiAIgiB0Agk7giAIgiAInUDCjiAIgiAIQieQsCMIgiAIgtAJJOwIgiAIgiB0Agk7giAIgiAInRDg7Q3QEnV1dZCVlQWRkZHQqFEjb28OQRAEQRAE1NfXQ3FxMaSkpICfn32bHAk7ARR1aWlp3t4MgiAIgiAIKzIzMyE1NRV0IexmzJgBc+bMgf3790NoaCgMHDgQXnvtNWjXrp3pM8OHD4cVK1ZY/N3dd98Ns2bNUvQ/0FLHf7ioqCiVR0AQBEFolUV7s+GRX3ZAveR17rt5++puMLpjkhe2jCAAioqKmOGJ6xRdCDsUbPfddx/06dMHampq4H//+x+MGTMG9u7dC+Hh4abP3XnnnfDCCy+YnoeFhSn+H9z9iqKOhB1BEMT5QW1dPby5bBM0Cg4zCTkRfO3NZZlwad824O9HYTqE91ASJuYzwm7hwoUWz7/++mtISEiALVu2wNChQy2EXFISraoIgiAIZWw8lg+nCytsvo9WPHwfPzegVbysMMT3coorICEyBPqmx5EAJLyGzwg7KYWFhew+Li7O4vUffvgBvv/+eybuLr74YnjmmWdsWu0qKyvZTTR1EgRB6BESH7bB38TVzy3cfRqen7vXQhjGhQfCS5d0hgldU+B8hY437xHgq9mrU6ZMgUGDBkHnzp1Nr1933XXQvHlzljWyc+dOePLJJ+HAgQMsNs9W3N7zzz/fgFtOEATR8MiJj+ToEJh+cUcY1zkZzndQeLjyOfxdJ3+/1SouL7+0Gu79cRvcfbIApk3oCOcbdLx5l0b1mEPrY0yePBkWLFgAq1evtpsdsnTpUhg5ciQcPnwYWrVqpchih8GJaA2kGDuCIPSALfGBoP3k4xt6nveTbVVNHbR/ZgHU2ZkN0di0/8XxEBTgZ7JIDX5tqV0XLjLzup4woev58/vaOt64rY6ON9dAfRIdHa1In/hcgeL7778f5s2bB8uWLXOY8tuvXz92j8JOjuDgYFOiBCVMEAShN1B8oOXEll7B1/F9/Nz5zJbj5+yKOgTfx88pjcvjPPPX7vPm97V3vPHX6HjzPD4j7NCwiKLujz/+YJa49PR0h3+zfft2dp+cTKsDgiDOP5SID54UcD7z6cojTsfYZReWK/qbvNKq8+b3dSYJhfAcPhNjh6VOfvzxR/jrr79YHZfs7Gz2Opomsa7dkSNH2PsTJkyA+Ph4FmP38MMPs4zZrl27envzCYIgGhyl4kPp5/TI31tPwbIDZxV9tnFEsOlxfmmV6skZ53MSCnEeCruPP/7YVIRY5KuvvoJbbrkFgoKCYPHixfDuu+9CaWkpi5WbNGkSPP30017aYoIgCO+iVHw4I1L0xIz5e+GTlceU/4HgQYwNC1I9OcPXs0obhwer+jlC58LOUY4HCjlp1wmCIIjzmTjBwqTG5/TE/J1Zzok6AMgtNSfb/bblhKK/iQoJYKLM2QSE5/7eA9lF5v+XFBUMz03spO3EA4W688cNx2FQm8ae3przFp+JsSMIgiCcIykqRNXP6QW0hj39126n/+6nDSfgr+2nYNWBs7DuqDmRwh49m8U6ZWlDUXfP91stRB2Cz/F1fF+r5JZYbrMt/tmdDW//d4CSKM53ix1BEAThHHkKYplQc/RqHuvy//BFlyFuL9aac5b1x/LZzRm2njjHfiMlvwl+buqcXXY/g+9jz1ot/saL9xpi35Xw/tLD8O364/Dq5V20bYX0QUjYEQRB6BAUCU/+YV8kiGU85FplKXMZ7oXsogoL699zE7VdiLYhg/eLKmpstiKTsv5IHhSU2Rec+D5+TmuuzHnbs2DuTuXCjo8Fa95RbTt1IVcsQRCEDll/NA9KK2s9JnTMLkPLv8XnWncZupLM4A5Kf981h3NV/VxDxive//M2l/6WaimqDwk7giAIHfL9+uMeEzpKXIbT5uzS7GSN7uLwIP8G+39Kf9+lB3IUfW7nqQLQCijgsX2aO1BtO3UhYUcQBKEzUFCt2H9G0WfDg/ygrr6eJQWsO5KnSIyhNdCRy/AcugyP5oEWwTGWVimzZroLRsIpiWHEbTpypljRdwYb25p5GyUCXynncy1FtaEYO4IgCJ2B1o+yGmXWsupagOs/36C4WTtO5r9tOqHYZTiotbZiwZDv1mU02P/CvbDpWL7DmDjcZ9UKDZy4j7SAEoGvFF+opVjrI4lCJOwIgiB0hjMxc1W1dRbPswsrbAa0o9sN46GU9EhFsgq0aYU5nl/WoP/v+w0ZDoWdM/sswE8bFrs3FuxV7bu0Xktxocyx72gR5C20cXQQBEEQmkgOsNWsHSc2FHxKRR3SNCYUtEjzuLAG/X+rDuU6dHGL7cocMXfnaa/HL2LCxPZTylzHvl5LcaGNY58vgrSWKETCjiAIt8AJBmOznInROt9o6N8IXUSxoa47ZKTN2nF7Ueg5u9UDNeiGRW4c0KJB/19JZa3D5IC6WuW/bl5plVeTDfB4eOpP5ws828OVWorlVbXw1B874eIPVsENn6+HFQdyVD+37B37thZB3oZcsQRBuAyuVKf/tQfOFJsrzidGBsPzl2i89VEDgRf7D5cehq/WHIOC8uoGc+Fg3M/Ll3VxO1uRuwdRRDhjqdN63BT+Pv5+uH8a7n9+tuqI3Vp2GzLyfCbZYMrPW1lyjJo4W0vxjm82weJ9llnEqw/nscSS967prtq55ejYFxdBrtSC9ARksSMIwiV4HTNR1CH4XOt1zBoCHH+vlxbBO4sPWog6ME4Env6NxnZOhraJ4aq4dF0VEdjvVEuWDA5Owg0p6pBl+89CVY29f+pcEP6L8/Z55RybMX+v04WIleBMjOHED1dZiTpOZU2dqueW0u1a5ETXDU9Dwo4gCKfByfqhn7fb/QzGnmhxUm9I0esoYxBLRXjiN+Ki8uCZUre+55zR4uaq5c3bLkMtdJ7g4F7+Zu0xm++vPXLWqe/LL6tq8PguFKafrLQ9BndoHK4sxvDvrSdh58kih5977m913KNKYx+/XJOhmcUsCTuCIJxm9cGzbGVsD7ykTpq5+ryL8XOmthcKP3TVekNUKuHFfwyTY1RooE+JKK11nuDM23naZqzY1hOFLn1nQ8Z3TZ1tfzHnFgoMljjOR2fvVPR12UUqFT124qfVSqwdCTuC8AGxoDU+XXVU0ee2nyyCNxbu99jvN3/naej90iK49rP1zIKI94NeXeLVlfOHSw85Jaq+XHNUtd+HB3qrBY8dmrsjy+dElKPkEm/UgttxslD22Hxl/l5Vklw8BR5Xaw7lwh/bPHde5ZZYhnTYqptX7USSybwd7l+/nVmYaKWDBiVPEOcN6EbAwqRYwwrLHWBmXJCkgjt+ZursHfDX9iwQrx+JkUHw/CWdKSHAyNYT5xR/9qPlR+DrtRnw1lXdVP39MNZHzi2UXWSI8ZvlhcbiOIF8sOSQU39TWF7DrHYPjWrj9v93NcnBHlnnytzqTcrduVpLnpjYLdljbkV7oPAe3THJorBtRp57dfU8aRV1tnahJxcAzrTJQ37YmMluWErluYmuJSvlllT5nIWaLHbEecHL/+yFtk8vgBf/2QffrjvO7vH5y//ssRAK+NqcbZaiDjlTXKXphICGtDBO/3sXlFc7F3mO7ZvU/P2whpajSdlT8Wv2+GDJQVDY8MECTLBQ47fxxKSy+US+1fngDA/+vE1zFm/8rb0h6mxZdVrEu1dXz1NWUVdqF0q5sEsSs47a8rTi6/g+WlEdbcuC3a4lKGQXuZ6sVFBW5XMWarLYEbrnzm83waK98hlUn63KgCM5xdAmMUrRhf7hX7Zbrba9DV6sMFAYL16c2LBAePnSzjCha0qD/ZZKwMbw7v5+KBKm/OI41gfdoeuP5Dms+K8WuF2frXJdLNz/4zY48JJ7v40nJpWD2e4lYNTU1cMDP26FmTf0svitcN+sO4qWwEasTET/lvENcl7h/35SYZyWp5AK8D7NYuG79cratEmJCQtkNeBwQadmqytXaxdabFtoALx/bU+WMYoCEbdI/D6+hVj6x972KknWUsKjv+5w+vrTyMmfsXtaDPiMsCsqcpyFwomKinJ1ewgvwi+2qw7nwI4TBZBXVgVRIYEwpmMS3DIo3cpt6QvM237KoRBZeiCP3ZSAlqr3Fh2ER8a2Ay3AA+WlYI0prGF298kCmDahoyr9DpX8lo7gjeFd6R/Kt3vlwRyoUmhCWo29ShtI2OG2udNYXk4ANUSRV7UtFnLM353NwhzwGoJxkU/M3gkllTWm9z9cdhiiQwPgtUldXXafKz2u8RqH7m9vIgpw3O4Z/x5w+btwAdP3lcUWcZ1q1ElUw63/ymVd2T7A7cAWdVKXbpLC7Xzopy0Ok7WUUFpVy0Ilpoxuq/hvBrRsDB8uO6L48z9uOA63D2kJPiHsYmJioJFC6Vpb6/rFjfCeQJg6e5dVvS1k8/ECeGXBfghoBBAeHABpcaHwyOj2MKxdE01ZrqTgBfOR39TP4np/2WHo2DTK6/F2SrIv0QrZLTUWJnRNNsV/fbLiEIjzWlSwP7sQ3X9BG5v7k1nJflXnt0TLgrPCzmCV3MPi55xh16kCaCjUcIOKAsgVNhx1rsitEk6o1Ff1m7UZkFtSYdMyjmLLXmykPeEmd3wkRQXDcxOtC2UbrITeIy48yMLtqIaAkibr2Ov3q5T/9rgXGnD30HR23eHgdqC1TLoPEXvWRjwf5u06A2rx+eqj8MBI29c6Kf1bxbNFh9LFQEP3IXZL2C1btsz0OCMjA6ZOnQq33HILDBgwgL22bt06+Oabb2DGjBme2VKiwa0+UjB2qLCiBgqziuG2bzZBoF8j+OC6Hl4XOLZAy5AbBhTVTfqeiOdSkn2J1hHksd93QJnMD1JUWQvvLD4EX6w+Cq9fIZ/gsPZQLqiwYGbUO+ncUXp8ypHpgYusLYHhTK9Pe2CCj6sr/jlbT4LaVKsUHzd3x0nYqaC3KC5WpOeWnHDDyfa2QenQJiES7v1xq+IkmjWHnKsXpzYvXdLZYmyeiIvEPdbIRqKG0mP8dxePpZAAP3j7qm6yYSC4HWJ3BrTePvXnLosuFlJB/r85Oz3S3m2Awi4RuM1D2zRWXJS5ofsQuyXshg0bZnr8wgsvwNtvvw3XXnut6bWJEydCly5d4NNPP4Wbb75Z/S0lNBdvghd8vHDGhwdCj2ax8O7VPSAiRDthm/d8t9lj340m/bWHc2FI2ybgDXCie3eJsvpn6PKSm/ikFFXU2rSYvL/MuUxPe6A1QSnuxtYczy93ywKmJJ4Rv3li12RIVKnh/bG8UrcmLa2iRNTJxUbaEvZoQcEFiTNCEY+FbQqK23oSP7+GCbZ3p9UV/k1xhWvH0hc391EU/qAkqx332z+71E9Yy3FCTOPx50ynjYbuQyyHS1c7tM717t3b6nV8bePGjWpsF9FATZDRquVuvEleaTVr79L5uX9h+BtLXMqAUzurs7CsGoo9PMn9viXT7X03bc4OGPHmMhjz9nKYNnsnzNly0uH4PR38PUWSxYgZqJsylJc3ccSSfcqPUTVia7B8jRpwgSGKOgS37s+dmGWprLafJ62MCVFBoAfWGLswsHCKX93bf1woIni+eRtpEVu0+MaGeW5B7IpFUHqMq/3/lGa14/zkbAa+ml0u1K4L2VC4dDSlpaXBZ599Bq+//rrF659//jl7j2gYbDVBRhfpTQOaw6iOSQ4D49ceUTfeJCOvAlr9b75TNcSw+On//tgFxRVmgYlbHBUaAImRIXB5z6Zw2+CWTlldLmuAjgenCspVzS49mFMKP20yiMW48EDmshnRPhFe+mcPbD9xDkqr6qBVQgQkRgZ7NPi7osYcxI/75oGf3GskLwXjOJVYEdSKrcHyNZN6pbECqK5mDDrTTcJdVhzMZSLSlRCHAA3HvDrDqXOGc+v9JQdlwwecBePqMFbKVueHhkRqRcNj8eYBLRRb4J3FFYvgr5ucqxcnYq/9HE/QU5rVjl4RT1BXr2xh6Ur8ozuhFF4Vdu+88w5MmjQJFixYAP369WOvoaXu0KFDMHv2bLW3UZc4m+6Pn8c4p9nbTrIL3a6ThXDaxqoKXaRfrMlgN1sBxJxNHqqSjZaNmdf1cFhuw1b5DDztULwUlpfAqwsPsBsG40ozPG39VkdzPR/Auvd0kcdKhuSXGrJapbhbyNSZIP6LP1gJuxS6z5wlS4EoxmB7tbj+8w2mx47OCTnQcqBGiy6luBIbhcf9XA0IFzXARD0cz6wV6lhBa+sNcZGVrhQZ9ABSi5i4qFUbZ8tv4IJq3VHXLfRxNmJNXSl07M7i2R4bjuUpCqNxxdqpheQJl1yxEyZMgIMHD8LFF18M+fn57IaP8TV8z9t89NFH0KJFCwgJCWHCU2vuYd6g+/ovNrA0akz1x4mn/TMLWINjuc93mb4QbvxqI/y5PQv+23vGpqizFa/w2K/b4dm/dsMXq46yE9cUBK6ii00KChMMjrUFFgd2pnwGmu4xLkPJJNwQlFXVwW1fbXTK1fzLxuNulwxpKDwl6pDtmY6Pu7k7T3nkf/NzwplipW/9ux8aEldaE+HncUGgB8qra9nCV40SF0hxeY0mOgJwVgsJHHht+Hmze2EdjspvOIO7Cyrs8qBWoeP6+noIw3IMqtPIY9ZOn0qekIIu11deeQW0xi+//AKPPPIIzJo1i4m6d999F8aOHQsHDhyAhIQEb2+e3Qw/7IH34K874NPVR2Deg8PczggU+X2reZLErgu3D24OYQGeT3TAoP1ZftZuWRSXWBzYWVDcPTqmvV23LAqohmLpgbMsLvCS7k2t3sML9sp9OfDs3N2QWaCdSUULOHKF4G+3J8uzQe5P/K4ssxmP1a2ZrjVodwdnhYiWhIu74DncOiFCte/DSl1a6AjA+XdPNrxeV8+OPVyIlnowHnjloVynXIObMly/fkaFBFh1kHCn0PFfOzxjgR6gMJmE9xRWKkjxUuJTyRM7d+6Euro602N7N2+C2bp33nkn3HrrrdCxY0cm8MLCwuDLL78Eb4MHOKbsO2J3VgkMe30p+/y9Kog6Ob5YfRw+WK686KI74JilwfLuBDEPfX2pxXP87lUHzrKg/7u+3Qz/7W1YdxRmbUqtP/i83dPz4dbvNp83og5jIpXi56AmJk52terHTFtlAT+kIH7w5i/XgzdQEuAtJh2dNsal6YGiihrIzFdvPC3iwzXREUBacqMhFqLbTpxzKhnNnd6+L1/WxWqh5In+xe5SqDCsAseCBZSV2gzvHKKNQv6Kr8Tdu3eH7OxsZvXCxxgDgWZS2dgILxUorqqqgi1btsC0adNMr/n5+cGoUaNYJq9SSktLwd/fX/XtQ7en0gKrWKZh+OtLWMadr4NjfvvfPXDv0HT2HC8yf2/Pcuv7pv+xA54Y0xoW7MmBqX/uVa3Gmqs8+ftOGNg8kl0I/t2bA4/M9r1MKncZ16Ex/LpVWVmADglh7DyzxTSVMlkdMW/XaWjy1054bFQr2fcX7DnjVryRO5SUltn9jRbtOwsz/j3E+hjrkX1Z6hWXXr4/Gz5c6pnkBFfJzC2ErkkhcOB0gcdF8vI9J6F/S/u9WPm1eWema9szom08XNA62uqYxXFqjXt/3ArvVnWC0R0cx9kNSY+Cd67oBDP+PQxniuXnbxR+twxIgweHNbd7zrqDM9/bqF5Onclw/PhxaNasGRNu+NgezZs3B2+QlZUFTZs2hbVr15oKJyNPPPEErFixAjZsMAdQI5WVlewmtk3zZFZvWIeh0GTiE4o/j7tGabcPrYNjKVj9PdScOw3+YTEQN+ouN7+vDipOHYCQpu1d/o3U/n2rC3Ogvq4GAmOSdbPfnNkfJ966AlInfwn+4Y4tI+dW/QBFa3+SfS+07SBocunUBvkN2eWPbfskgDrLAPbQtgOhySVPQiM/dRZ5JftWQmjLPuAfrKzeXfnxXZDzs3mRarltA6DJpf9jj5X8Tvwy70vHZV1VBfgFqeM+dXb89eidatRI9vNq/ZbZP06DypN7IPXBH8E/RD23sxz1tdVw9u/XofygfQNHcFoXSLrO+SYDJXtXQt7c11X9Tk9SX18PdeVFcPLDG9n5r4hGfhCc2gn8I+LAPywWgpJaQqPAELYPi7f+Y3X98BSFhYUO27YqttiJYs1bwk1tsEvG888/32D/r7bEuZW/L12ElRA75EbVvqtRIz8ITe3g1neU7V8DIendLS6qtVWVUJm5C2oKsiGq10VOfV9gtPdjOL11kSza9Bf+eFC0dR7EDrnB4d9E9b8Sitb/Zn0xbOQH8eMecOrYr0cPgZ+fS+cL+5tG/hDZ40Io3vKXRDhNU+0crKuthby5b0LMiFshus9liv4mOKUt+z2sJp5GftB4wsPm7VdI1ZkjEJzUGrQOF05qiTpnf6fa0gIo2b0EovpebnfxJ/ee0sUiCsfKU/sgOK2zx0Udwy+ALQTO/vmKXXHnH+Far+Gac7YTnVD44G+qZMHXUDRq1Aj8w6LZ7195wtnwsXqoyjkCxVv/Vi4KGxjFFjsRbB3WuHFjuPDCC00WMew4gTFtP/30k9eEH7piMZ7u999/h0svvdT0OnbCKCgogL/+Ml+47Vns0PLnSBG7Apq5e85Y4XW3IWHgi+u7Qp8WsbDlRAGcLamCJhFB0KtZDHOn4r4a/OYqKKqkneWI1JgQ+PeB/uzxP7vPwBN/7FP0d7GhgTD9wrYW7hAMV7j1O+Vu2C5JYfDD7X1gwOsrobTa9VIWnZMj4Jc7DEXXcd/3f2O1KvXTOE2jg+G/Bwc4Pb6vbuwGfVvEmrYLC0XP3p4F8/c4X98rIsgfSjzUY69TcgTsOV0CeuDtSR1hbMcEeHPxEfhmfSaI4Wko2W7qn8piRL9a514m65OjW0F+WTV8tuYENBTYhm3VI4NsJgx9uPwYfLzK+Rp2dw9uBg+OsJ2gMeW33bBov3d79Mpx56A0mHKBfBiGddiDpSsW64lOG9takTtXDVCfpKSkqGuxE8Fs2I8//pg9xti1Dz/8kGWfzps3Dx5++GGYM2cOeIOgoCDo1asXLFmyxCTsMOEDn99///1Wnw8ODmY3KeHh4ezmCZrHhcORXM/44D3BmI4JsObwWSit0kb9J7UI8m8EwzulsgvciE7yK+bXr+yuSkaynokPC4DVU0eanqc1jlb8t+fKq+Hh3/dYNCovqHIuvmdiz2YQFRkBM2/oDTd/tQlcZffpEvALDIHQIH+49/vNqoo6JL1xBLumDO0QBlEhu1nihhKKqhuxv8NkHCyQ7E4tPRR1aExyfinvGCykrQdhN7pjAlzexxALPP2SrjDtws6s4CzWJsMyFpjxiNeMwa9ZJnC5wmuLjkB4kPqx3PbA2qC7zlTAoNbWLb9w4fD1etdE5tD2yXbnzFaJkZoUdjnF1Xa3G38TjM18Z/FBmb+ttLp+eRJnchdcSt/IzMyE1q0NJv0///wTrrjiCrjrrruYa3PVqlXgTbDUCXbFQKvivn37YPLkySzoELNktcDVfXyrM0dYUAC8dnk30Bv3DG3lsMwFnqzvX6W/satFWkwwbHl2rFV5gEB/11ss5ZcoSy7i3DzQMAkPbuP+qrnDswtZUeb5u93vdiHlTqHchDMWe8yM5SWP1CiQPEyF30mOAS0bs8LPvs7uU0UWGaSY4YilQl64pDO7x+dqZnliz+mGxlYWLnZ5KHfB6h0bFsiK69ujyIOdctwtxL7QRj1LfH3Qq0tkRR1Sb7xJW8RpAZeEXUREBOTlGQ6O//77D0aPHs0eY0Hg8nLvptxfffXV8Oabb8Kzzz7Lsne3b98OCxcuhMTERNACtwwyTES+QkpMCFzUvSlbyeoFlHMPjW6r6LMTe6ZCzzTlVqjziUt6WC9SUCx3T4t1qVE5EhOmvNfphM5JptIC+H/Rra7FoszBAX4w2FjlHovuOmMNrKmtg0cUtF9SSlpcKOvgombnMazzhe26rvGxRaurhaF9v16gtQhhi4cftrj0bTMuty5xIuWsRjO3q+sMXZLkylVhQWUlVSxcKSauSWGHQu6OO+5gN7HbxJ49e1jHB2+DblfM3MX4OcyE5W3PtABORHhh9RUGtTJMSJ/d1IfV6NEDl/VIcapV02+TB4Fe6dw0SvUinw+OaOP0d/HJ0l6fSRHcfR9c19PitT4tHJdz8AbvXdPddLwZWggq58V/9kKZqk3QG7G2fPtfHA/PXNiB9ZS+sX8zN74NWJ0vHJ9eYoel7b6kaKnQsSv0axEvK2KcLZKMgl5pT/CI4IZ1OTsLhjlwq5srBZUdHTM+IeywZReWEzl79izrDRsfbzhQsIbctddeq/Y26g68sKoh7jBObFCrOOjhIYtSSIAfW4lznrqwIxx8aTw8NaE9jOmYCJd1T4EHL2gt20JGy7w6yTn3Kk5avuSSDQ/yY/vFkXTFZJF5DwxhF2cMBFbL/TKwTWMIdPLKgi5HvKB+sFTe7SFldMdEK3EuFzfkaRoZhVuMTHFmDFS3nvicM5UdPqtuPG55VY2Vi/F/CvovyxETGiiJL9KWO8pVHIUD8G4EDVmzAGPxPrymhyrf9dOmE5Ki+c53hfjm1j6w+skLFMeWXd4zFTxFgArm54KyamZNR1xxtefaqG/nLVxKnoiJiWEJE1IasnSIHsTdlFHtoOOzC12+HD45rr2pVczcHVnwvz92qdpM+p5h1nFoOCHcObQV3DnU/NpDo9qyk+GleXtgz2l1XFmYnYrZqmrjamVwdMm+s+QgHMtzP9QA/3vH5EhWJysmLBBuH5QO0/7Yrdqqb2ynZHhkTDu2X66atVb2d7ygXTx8eashkxUvzthaC/fhrBWHYcXBXLfcL/j6xd2SYc425R1APlh6CG74YoPic6GNTLspFJr4e6oRi6aUj67rCRO6JsNFXVPYxGCwyDVi1kzcHulvhK9jb2hvsXh/DpvMxe1ytpco574RrSwmdoyzw97Xvo6jcADejQCtXPgriscsf46iHhMV1OKuoa1gTOck1eLKsE0eXgen/LzVpetOUIC/U16Pga0bQ5AfQJUHrLqXdEuG2dtcL3jPWXPkLAxq0xj+2+N856JzZdoSdi73vsAkiRtuuAEGDhwIp04Zath89913sHr1ajW3T9dgBt79wx2nWsuBp5TYk+7ibimw/dkx8NOd/eG2QS0gDM8iNwj0bwQPjFTmUsMTHCesfx4aCpOHKe9JaM9S+NNd5gLTaoFxgmh1dJXFj45we3WYEh0Mh16ZAPMeGgrzHhwC39/RH0Z0SITnJhra1tj69mZxyoraIknRIab9MvveQbDvhXHM3TakTWN2j8+5qJPuw29u68essk+OawvJUcFWsVhK3S8lTpaJWX8s36kFDooIKTiGVy/vAg0Fnmco6vj/xknhsbHt4bGx7Zj1UG7iQ7EX1sCZkFaWiaOWwfOY8ekKjSMsrbxo3ffm2NSioMxxOAAe/2it5OcaJ8l4fgxto571OCI4AO6/oDXLzlWLaXN2woz5e2HuTmWdYtyNM8RzYaJMP213wSzvGZO6qeIByyqoYIue37acdPpv/bDepK9b7ND9euONN8L1118PW7duNdWCw/oqWApl/vz5am+nbpkypp1LPVvHdU60sjzxyRlvKGBECwLOMe870VLn7avMcUHOgBPbl2syoNKNgJtJvZoaLINDWsBnq9y/mLGxX92dJYG4A/4eH17Xw60SKK9N6ib7u/KJAmM7RDcACim0Dqw+dBa+36Csbpb063EB8eKlygUP/vaTh7dhN7zQoSUPL+QYW4RuKCXHhSfLOPj7GUSEHPg74sSK7iXREhEW6KdqrFp6fCg8e3Enp/8Of7u7h7aEdxYfAm+B2Y+i2xrLeLhCUnSo1djQIv7eEm217nKWuHBlCTyipVs8P5AnZ6vXM71Peiz7bV0V4HL8vf0USxxwFVfiDAe1aQK/b7VdyNgVQgMNlkP0gHVLjYUnZu+EkkrXLKWJ0cFsX2IfX7XijX1K2L300kswa9YsuOmmm+Dnn382vT5o0CD2HuF8/NaDvzrXG7NnM/sZgNyCgDdO+6RIuO/HbQ4tI6M6JDALoCvg/8WYI3fED28Q/9SFnSAjrwwW7c1R/LfpcSGQHBMGp4sqICU6FO4a2pKVwnBFpNoXDnsU9/3lhAf7M5eEsxMFbjsGNisVdnLWLFfhiwVnwZiaP9zoB2yPNk0i7O5Pud+xV/NY6P78v6qIu0ZG662r3H9BG/hqbUaDuoxFTp2zDCdAy//L8/dZFOJ1BC44uIgR6ZuOx0rDCLtJPZvCkn1noEDlUhpSwers+YHlRNR0w27JOMcWWK4KcDncOQ3iw4Nk970jEiQWXjXADHM8z3EfoPV8bOckk0Fjw9E82HRceTjPjxsyoabGtcAorSVuuWQ/PHDgAAwdKgRZGYmOjmYdHgjn47fSYp1bAWVKLs5KmNA1hcUE2WNUhybw+c19QA3x42xAPkcsl4HZuB9c2wNkYtPlJ9zHLoAf7xoAyx4bAT/c2R+GtUtQTdSJ41szdSRzew9v20RxEPVbV8pb6+Qmiku6N2X3/PMpMaGK3Ta2rFkNCQpYT1ntpo1z3EpO+juiFfLtq7ur8v/fv7aHW8dUQ7uMrbGcvAzW8XSXMmGl5DpZh9BV8D/PuLwrbHlmDPxwez+4Z5g6GfuYvemKaPFkOZSiihomXsTQG29ySXfnqgpw6jxRGVvye4shETc4+XthfPoXa1zzEG057ly7UE0Ku6SkJDh82HpVhvF1LVu6H2N1PvL6Fc5NOq6u3nBVg6JLWkwUL2gfXtMdPr+5L6glftZOM4ift67oymK7uqUqy96Vihi0Hu5+YQI8PMp+7Tl0Zaot4hwJh69v6wsHXjKUjriBxbHFWwkaZ8oCOMrEc8Trk7o22G9gD9yGtzyQSYxDG9zOtSK7+PvfOrC52+3TXLVmi6BFERM9vEFTmWsHz9R3dOjgMWiv0n5DlQK5sGsyE6R8Ip86viNc1MX9WqVDVLDue+I3QPGC26WFSC48dl1hg4dqvdn6vRMasCyN1mobuuSKvfPOO+Ghhx6CL7/8kjXTxd6q2Frs0UcfZYWBCdcm7tiwADhX5tiEj55Kd1Zv9lx+amJ2U8TDpN5pzJ3Q66VFdl1Qtlw8+F0PjWoD7ZIiYPpfeyx69qFIfW5ipwZp6yIHLx3BcTUuTWkmnq11L07MPJhfC+D+eHhUG1Xjyd652rXYT86YTsnw1VrXskARR4sLpeDx4S1X7EAbrnoUd4+OaW/RQuu6fs1he2aB4mOZL0CyCys8VvwkkIV7WJf+eO/aXrBw93xw0ZvGuKG/+33O8TdQOysWf3s8ZrxdKhAXI65bNNU/IvBQxDALd+dUd9FabUOXhN3UqVNZD9aRI0dCWVkZc8tiz9XHH3+cFS0mnAcvli9f2gXu/XGbw8/eMdi1kh3S/9fQAZ/cBWVLnNhz8TS0KNXib2srwSIuPBBeuqQzc7VrDYwnm7nsMFTWun9R79I0irlW3YEdK40AXN2clNgwTa7w0eLeLz0Oluw/63Bitueqly5SEGeOZXulQNRiVEf58Ap87dIeTV0O0FfSGksJuB2YFetqxqmU0EA/dtzO2+mZmFVnuMXYK9cVPFEOB+NC0Q0qd4z6OzGnuoMtY4Q3cUkdoJXuqaeegvz8fNi9ezesX7+eFSvGGLv0dH10J/AGODE7Stt2t2SHt+HiROpWdOTiURKHdj6Avw8WBkUXNyap4P2mp0ZrUtQhuG8u6ua+FTE80A/mPjBEle1pK1MDT2m2pFoXcLVW+Fjv8Yc7+sGO6WPhi1v6Omz9hwsrT58vtkqByJXOwetdVIhzsZjX9bFtVQsLdslWobg1lhLQYr8pQ72Yq2FtDe5hLViFbFnHlIALCk+EH9hbJE1QMKe6iyNjhDdw6izAsibPPfccLFq0yGShu/TSS+Grr76Cyy67DPz9/eHhhx/23NaeB/C07af+3AXnBFcNrshfvayL2yU7tIAvWN20jDesre4w4/JuMHure9YG7JCgFlPHdYCbv9nk9N9d6mLQuCfddViIWixdgslGWKwc65SJZRsaOlzBVmYyWlek5/wT4zrA9Z+tZ7UMleCHJlcVY495SSG1fhscs7MZ8/a4sb8h7AZ/L9yPan63K3FyQ4x9j1312LhTMUEOR4J32oSO0CUlBh74ZRuomb+Bl4IPr3UvdloTwg7j5z755BMYNWoUrF27Fq688kq49dZbmcXurbfeYs9R3BHuwdO29Sx8fE2cEK6D7r2R7Zs4dBM2hAsUweQLjGRwttTiyA7uB+eLx//Idk1gznbnq9xbZEDLuA4xuWNCl2SvXz/kznFbLjPMYO/4zAJFLnt7mbcYe/zSP/sUu4Ax6emWQemq/jZqutmx4DN3neM2ojhXWxg5R71HykVFhwRAoQtdk5Ra0eMjg1UVdciH1/bQVEyzy8Lut99+g2+//RYmTpzIXLBdu3aFmpoa2LFjB3PPEupBwofQE3cMaeWysFM7hsVQaLqn8xOkyhNDXb1710x7GdC+dv3A7b13RGtFiTb2LDS4iLhraDp8svKYouNKbVHnaPucZULnJIvtQ2E087oeHo8b82SNTFsem0V7s2HqnF1OJRUpLb2So3JMKyZRaTX8xekYu5MnT0KvXr3Y486dOzN3LLpeSdQRBGEPvHBjkodWYlj4BOkMuaXqusDKqp2vcC/GXWnVWuBOoo29GKxGCkU+L91iDyWJWq6C2xcTqk4smehm56CgmOmgHqkncJR44wxycdJ4Tm55ejSrSzhI4f9JVVjfM0Hl+MTJLrYC1aSwq62thaAgc7uVgIAAiIhwLRCZIIjzB7xwY+aus5063K3/Zw9nJ0i1Jwd3qtXfM0zbE4s7MVhyUou/plSMobjDnsfYnSJYUkHAmUQtV8Dtu3VQC492wbBVj9STNETiDa9LeEWvVFXbv/U1ZsOrhdYKErvliq2vr4dbbrmFWeqQiooKuOeeeyA8PNzic3PmzFF3KwmC8HlYhtrJArtushbxodAjLZa1JMPuFZ6eSHCCnAn2XVu4BUkeKGlw80BDKy89lFfwdEmfJBcSHNAt+9ZV3eH1K7o1eLwhWh9nrTgM5dWu+++jQgLs7mfu0vx6zTF48R/njyOleKNOqNK2bs60f/Nzo8yR1gsSuyXsbr75ZovnN9xwg9rbQxDEeZD1/fRfuyG/tEoTtfiY5Q4awb0/bnXbUuQMKDzaJobDwTOliv/Gky5EvWbNe6tm5zV9mrlVDLtHs1hFLQgbu9i6UQn3j2gFD49u1+DHGy90LYp7dxY4G4/lu9UfV4oWSs+oJuywrAlBEITesr6Za8tPHUuRM/XOCp0IFA/0b8T6JmuxvILa+FryhxypbmZyD5aJr2tokTGotfst1jzRacfZBU52kXoWNjX6CXsa16s5EgRB6Gjibuj6ivh/zhSbrZaOuH1w+nkh6vSC0vgvWygtpO2pNm6OXMHecsu7UncwV2hB6S53DG6peYs5CTuCIAgvCE5n43Rw4iZ8B2fiv+TYdPwcDGtvv5OIJ9u4vXyZ55MlGmqxla9SRjvWFXxgZBvQOu41HCUIgiBcwlkXWlOFpR0IbcAtaa5T73YbN3cSJrDQtRZQo4VktkqLorev6uZ1sasEEnYEQRBewNl6Z5glTPgO3JLWqIGKAYt9pN+5qptbruBJPZWVG/EVUmLdWxTFhAZ4tPSS2pCwIwiC8ALO1Duz1T6M0DbckuZsce6QAD+XigFz6xa6gcWsc2cZ2Epfi4iBbnbMKHCzp3NDQ8KOIAhCo90WlLQPI7Qv7tZPG8UKbjtTgNqd/Z1dWO7y3+J/7aPxrE9n6d8qXtF5Zg9sd4aZ7L4ACTuCIAgNdlvgYHssvbUPO9/AmoUj2jZWbK1zN0DfHWtdvQ90VnD1PHMH7GG7/kge+AIk7AiCIDTgrpMG2qP7DvvZYlFnwrdBS8+yA2cbxFqHxEUE67qzgqvn2Sw327CtO5oLvoBPlDvJyMiAF198EZYuXQrZ2dmQkpLCul489dRTpt61+Jn0dOvGz+vWrYP+/ft7YasJgiC0WUOPaFjWH82D0iplrQ/Sm1i26HSFpCj3smMbuykMtX6ejX9vJRw8U+LCN/jG+egTwm7//v1QV1cHn3zyCbRu3Rp2794Nd955J5SWlsKbb75p8dnFixdDp06dTM/j4yngmCAI7aPFos2EOqxzwoWnhqjCRUFoYCPXe9X6RiiZy+dZVIhr0qefj8Qe+oSwGzduHLtxWrZsCQcOHICPP/7YStj9v717AYqyXOMA/qyC3EFQbspFGfOKKaAgmJqRcMZpzJRyZPTAmS5mmqadHDUnszONGjlNmXlsMDLTIhoLb5M6KlmGNJg6Gd5viZe0FIFRMeE987xnlnZX1I/YC++7/9/MKu5+++3+3WW/Z7/vfd6PC7mIiAgXPEsAAIAWVkrCPsVLlxA/OvS39koR/W6nCX1bq4zeEVR+pop0pewYu2vXrlFIyJ3V86hRoygsLIweeughWr9+/T3XUVdXR9XV1VYXAAAAe2rOnHT2KqqiQny1Pcl9S+UOvnPYlhFlp66QCpQs7I4fP05Lly6lSZMmNV7n7+9PS5YsoaKiItq0aZMs7EaPHn3P4m7hwoUUFBTUeImOjnZSAgAAcBc83YbR6U7sVVQld/17h/W5iae1n+TeHl3KCdGBzb5fgzA2TtKtC7vZs2eTyWS654XH11k6d+6cPCz75JNPynF2Zh07dqSZM2dSSkoKDRw4kBYtWiQbLPLy8u76+HPmzJF7/syXs2fPOjQvAAC4Hz40mjf2QacWVTlpxia/tsVny3CHpp1/Z/Zq9n2CfdVoKnHpGLuXX36ZcnNz77kMj6czO3/+PA0fPpzS0tLoww8/vO/6ucjbtm3bXW/38vKSFwAAAEca+WAnmlRZRSt2nWrydpOdiyreK5UaF0ylJ43PSdcrMkCZ02a11KC4DuTtYaKbt40PauwYoEa94NLCLjQ0VF6M4D11XNQlJSVRQUEBtWlz/52N+/fvp8hI93iTAgBA68ZzEvaLCqZ5xQetJhHmPXVc1Nm7qHogPLBZhd2A2GByF23bmGRxV3L0d6dNI+MsSnTFclH38MMPU2xsrOyCvXz5r4kezR2wq1atknPaJSQkyH+vW7eOPvroI8rPz3fZ8wYAALDEZxHJjHfOnIWxzWygmOtmk2EPeSDUcGHHU6SoMvZQicKOD6dywwRfoqKirG4T4q/dqDyJ8ZkzZ8jDw4N69uxJhYWFlJWV5YJnDAAA4No5CyemdqH/bDpkaNmkmPbk0874+Wx1kJ0Sa/j/Z2xiZ2XGHirRFcvj8LiAa+pilpOTQxUVFXLSYm6EKCsrQ1EHAABui8fZxXc21v35z7/ZbKGy/WeNz2WX0UedYV1KFHYAAADQ/HPUVl65bmjZEN//n57TnVwyeE7c9r6eyhyGZSjsAAAANMTj+Kpu3Da07OGLNeRuwgzOGfivtK7KHIZlKOwAAADceI8UO3vV2J49nSR3DZEdyab77K2b+kg3UgkKOwAAAA015ywWze2g1UHbNiY5zQy7W3G3aExfpfbWMRR2AAAAmu6RCg+4/9g5rlu4g9Yd/SM+kpZPSKSIIOsimPfk/XdCopITNisx3YmzmLtsq6urXf1UAAAAWmxWeizNKDxwz2VyBsfSzeu1ZPzArV7SYvxo8+QBtPf0Vbpce5NC/b0pqUuw3FPXWuoB8/OwnA3kbkzCyFJuorKykqKjo139NAAAAADuwOe0t53P1xYKOwsNDQ3yfLQBAQFkMql1TN1Itc9FK78pAgONzWukEp3zIZuadM6mez5kU5PO2YQQVFNTQ506dbrvKVVxKNYC/2fdrxJWHb/ZdXvDu0s+ZFOTztl0z4dsagrUNFtQUJCh5dA8AQAAAKAJFHYAAAAAmkBh5ya8vLxo/vz58m8d6ZwP2dSkczbd8yGbmnTO1hxongAAAADQBPbYAQAAAGgChR0AAACAJlDYAQAAAGgChR0AAACAJlDYKWThwoU0cOBAeWaMsLAwGj16NB05csRqmZs3b9KUKVOoQ4cO5O/vT2PHjqXffvvNaplp06ZRUlKS7Bzq379/k4/FPTVvv/02de/eXS7XuXNnevPNN5XP9vrrr8uzithe/Pz8lM/GtmzZQoMGDZKPFRoaKtdz+vRpLbJ98cUX8jZfX1+KjY2lvLw8cjR75Dtw4ACNHz9ezojv4+NDvXr1onffffeOxyopKaHExET5f9CtWzf6+OOPtch24cIFys7Olp8lPAn8Sy+95NBczsy2bt06GjFihPxd4wlxU1NT5e+gDtm+//57Gjx4sFwHL9OzZ0965513tMhmaffu3eTh4XHXzx0lcVcsqCEzM1MUFBSIgwcPiv3794uRI0eKmJgYUVtb27jM888/L6Kjo8X27dtFeXm5GDRokEhLS7Naz4svvijef/99MXHiRNGvX78mH4uX6dGjhyguLhYnT56U69q6davy2WpqasSFCxesLr179xY5OTnKZ+PXycvLS8yZM0ccP35c7N27VwwdOlQkJCQon23z5s3Cw8NDLF++XJw4cUJs3LhRREZGiqVLlzosm73yrVy5UkybNk2UlJTI57569Wrh4+Nj9dz5tfP19RUzZ84UFRUV8ra2bduKb775Rvlsp06dksusWrVK9O/fX0yfPt1hmZydjbMsXrxY/Pjjj+Lo0aPyd8/T01P89NNPymfjDGvXrpWPw68hL8Pv0RUrViifzezq1asiLi5OZGRk3HVbqCIUdgq7dOkST1Ujvv32W/nvqqoq+aFSVFTUuMyhQ4fkMqWlpXfcf/78+U2+mXnDwhvRw4cPC92y2eIPD17Hrl27hOrZ+P78utXX1zdet379emEymcStW7eEytnGjx8vsrKyrK577733RFRUlGhoaBDO0tJ8Zi+88IIYPnx4479nzZol+vTpY7XMuHHj5IZO9WyWhg0b5pTCzhXZzPiL4oIFC4SO2Z544gkxYcIEoUu2cePGiXnz5hneXqgCh2IVdu3aNfl3SEiI/Hvv3r30559/0qOPPtq4DO8+j4mJodLSUsPr3bBhA8XFxdHGjRupa9eu1KVLF3rmmWfoypUrpHo2W/n5+fIQ0ZAhQ0j1bHwokw91FRQUUH19vXyc1atXy/V6enqSytnq6urI29vb6jo+zFJZWUlnzpwhZ7FXPl6PeR2Ml7VcB8vMzGzRe7u1ZGsNnJWtoaFBnqjdmfmdlW3fvn30ww8/0LBhw0iHbAUFBXTy5Ek5obFuUNgpij9AeKwKj4GIj4+X1128eJHatWtH7du3t1o2PDxc3mYUv9l5Y1lUVESffPKJHOvDv1BZWVmkejbbsRpr1qyhp59+mpzFkdm4CN+6dSvNnTtXjtPi9XHhw2PTVM/GRQ6PZ9q+fbt8nKNHj9KSJUsax3CplI83joWFhfTcc881XsfL8n1s11FdXU03btwglbO5mjOz8bjk2tpaeuqpp0iXbFFRUfLzZMCAAXJsG3/JVz3bsWPHaPbs2fTpp5/K8XW60S+Rm+BfsIMHD8oBro74heI9JFzU8d4stnLlSrlHiAey9ujRg1TNZumrr76S365zcnLIWRyZjT/Ynn32WZmHBw9zttdee00W5Nu2bZNNIqpm41wnTpygxx57TH5j54Hq06dPl80wvJfSGeyRj+//+OOPy70EGRkZ1FogW8uzrV27lhYsWEDFxcVy4L8u2b777jtZrO7Zs0cWQ9zYw58vqmarr6+XzTz8Wpm3b7rBHjsFTZ06VR4m3blzp/w2ZRYREUG3bt2iqqoqq+W5Y4hvMyoyMlJ+i7F803NnEfv1119J5Wy2h2G5ULDdU6JqtmXLllFQUBC99dZblJCQQEOHDpXfSHkvV1lZGamcjYvSxYsXyw0M703mIjY5OVnexsMGHM0e+SoqKig9PV3uOZg3b57Vbbysbacw/5sLWD7krHI2V3JWts8//1zuyeK947aH1FXPxkcC+vbtK79czZgxQ36ZUjlbTU0NlZeXy8fg7Rxf3njjDdlNyz/v2LGDlOfqQX5gHA8SnzJliujUqZPswLJlHlj65ZdfNl7HDRDNHai+ZcsWeR/urLRtMjhy5IhQOZtlFyI3FWzYsEE4mrOycUdlcnKy1XXnz5+X69m9e7fQ4XWzxB20qampwpHslY+7/MLCwsQrr7zS5ONw80R8fPwdDSOObJ5wVjZXNE84Mxt3jnp7e4uvv/5aOIMrXjczbgqJjY0VKmerr68XP//8s9Vl8uTJchYI/tmyA1dVKOwUwm++oKAg2cZtOV3H9evXrVrBuT18x44dshWcN3y2G79jx46Jffv2iUmTJonu3bvLn/lSV1fX+MZPTEyUU2VwyzuvJyUlRYwYMUL5bGbcCcUfHrdv33ZYJmdn4/Z/Llb5w5c/FHm6Ey4M+IPY8rFUzHb58mU51Ql3wPH1PJ0Bb0zLysocksue+XhjERoaKrsJLdfBHX+2053whogzLlu2zOHTnTgrGzO/nklJSSI7O1v+/Msvvyifbc2aNbITnV8vy2W4AFE9G08/xF31/FnCl/z8fBEQECBeffVV5bPZ0q0rFoWdQvhbSVMXnvfH7MaNG7K1Ozg4WG4ouD2d39S235qbWg/PVWR27tw5MWbMGOHv7y/Cw8NFbm6u+OOPP7TIxoUrT5Mxd+5ch+VxVbbPPvtMzlvn5+cnP9xGjRolCwXVs3Fhx/NVcS5eR3p6utizZ4/DctkzH280mlqH7Z6PnTt3ynne2rVrJ+fWsnwM1bMZWUbFbHd73zpyXkxnZePphHgKHr5/YGCg/Fz54IMPrKZTUjWb7oWdif9w9eFgAAAAAGg5NE8AAAAAaAKFHQAAAIAmUNgBAAAAaAKFHQAAAIAmUNgBAAAAaAKFHQAAAIAmUNgBAAAAaAKFHQAAAIAmUNgBAAAAaAKFHQAAAIAmUNgBAAAAaAKFHQAAAADp4X/kQZnIKV8hFwAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 4 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from statsmodels.tsa.seasonal import seasonal_decompose\n",
    "decomposition = seasonal_decompose(data['Close'], model='additive', period=252)\n",
    "decomposition.plot()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               SARIMAX Results                                \n",
      "==============================================================================\n",
      "Dep. Variable:                   AAPL   No. Observations:                 2485\n",
      "Model:                 ARIMA(5, 1, 0)   Log Likelihood               -5148.449\n",
      "Date:                Thu, 02 Jan 2025   AIC                          10308.899\n",
      "Time:                        15:47:53   BIC                          10343.805\n",
      "Sample:                             0   HQIC                         10321.575\n",
      "                               - 2485                                         \n",
      "Covariance Type:                  opg                                         \n",
      "==============================================================================\n",
      "                 coef    std err          z      P>|z|      [0.025      0.975]\n",
      "------------------------------------------------------------------------------\n",
      "ar.L1         -0.0143      0.013     -1.126      0.260      -0.039       0.011\n",
      "ar.L2         -0.0249      0.014     -1.808      0.071      -0.052       0.002\n",
      "ar.L3         -0.0275      0.014     -1.912      0.056      -0.056       0.001\n",
      "ar.L4          0.0105      0.013      0.808      0.419      -0.015       0.036\n",
      "ar.L5          0.0137      0.013      1.042      0.297      -0.012       0.040\n",
      "sigma2         3.6965      0.053     69.727      0.000       3.593       3.800\n",
      "===================================================================================\n",
      "Ljung-Box (L1) (Q):                   0.01   Jarque-Bera (JB):              4080.43\n",
      "Prob(Q):                              0.93   Prob(JB):                         0.00\n",
      "Heteroskedasticity (H):              43.69   Skew:                             0.06\n",
      "Prob(H) (two-sided):                  0.00   Kurtosis:                         9.28\n",
      "===================================================================================\n",
      "\n",
      "Warnings:\n",
      "[1] Covariance matrix calculated using the outer product of gradients (complex-step).\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/titiksha/dev/cla_christmas_break/.venv/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:473: ValueWarning: A date index has been provided, but it has no associated frequency information and so will be ignored when e.g. forecasting.\n",
      "  self._init_dates(dates, freq)\n",
      "/Users/titiksha/dev/cla_christmas_break/.venv/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:473: ValueWarning: A date index has been provided, but it has no associated frequency information and so will be ignored when e.g. forecasting.\n",
      "  self._init_dates(dates, freq)\n",
      "/Users/titiksha/dev/cla_christmas_break/.venv/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:473: ValueWarning: A date index has been provided, but it has no associated frequency information and so will be ignored when e.g. forecasting.\n",
      "  self._init_dates(dates, freq)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from statsmodels.tsa.arima.model import ARIMA\n",
    "\n",
    "#Data Preparation\n",
    "data['Close'] = data['Close'].dropna()\n",
    "train = data['Close'][:-30]\n",
    "test = data['Close'][-30:]\n",
    "\n",
    "model = ARIMA(train, order=(5,1,0))\n",
    "model_fit = model.fit()\n",
    "\n",
    "\n",
    "print(model_fit.summary())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/titiksha/dev/cla_christmas_break/.venv/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:837: ValueWarning: No supported index is available. Prediction results will be given with an integer index beginning at `start`.\n",
      "  return get_prediction_index(\n",
      "/Users/titiksha/dev/cla_christmas_break/.venv/lib/python3.10/site-packages/statsmodels/tsa/base/tsa_model.py:837: FutureWarning: No supported index is available. In the next version, calling this method in a model without a supported index will result in an exception.\n",
      "  return get_prediction_index(\n"
     ]
    }
   ],
   "source": [
    "forecast = model_fit.forecast(steps=30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1UAAAIjCAYAAADr8zGuAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAm5pJREFUeJzt3QV0VNfWwPEdN5JAIIK7u1tLoaXQlnq/tq8CtVd3l9dXd3l1e30tdXeBFijSUtzdXUKCREiIz7f2mblDEuKZZOz/W2uYm5nJzJnJDbn77n32CbDZbDYBAAAAANRIYM2+DQAAAACgCKoAAAAAoBYIqgAAAACgFgiqAAAAAKAWCKoAAAAAoBYIqgAAAACgFgiqAAAAAKAWCKoAAAAAoBYIqgAAAACgFgiqAMANZs6cKQEBAfLNN9+45fU/+OAD8/rbtm0Tf3L55ZdLmzZtStymn8MjjzzistcYOXKkuXjzZ1LRYxs0aFDnYwIAb0NQBcBvrFy5Uv7v//5PWrduLeHh4dK8eXM5+eST5bXXXivxuKeeekp++OEH8VQaCGkgYF2CgoKkVatWcs4558iyZcvEU3nruMuyZs0aE4j5YlCanZ1t3psG/nVp0KBBZj946623Kgz8rUtwcLD5ndXAbvfu3cc8XgPZHj16lLhNg0X93tGjR5f5Gu+++67z+RctWlTmY+655x5z/4UXXlij9wnAPwS7ewAAUB/mzJkjo0aNMgfxV199tSQlJcnOnTtl3rx58sorr8jNN99cIqjS4Ovss88WT3bRRRfJaaedJoWFhbJ27VpzcDp58mTznvr06VPh944fP17+8Y9/SFhYmHjTuOvCkSNHzAF7dYOqRx991BzIl87yTJkyRbyJBhZFRUUlgip9b6quMm4bN26UhQsXms/u008/leuvv77cxz722GPStm1bycnJMfuIBluzZ8+WVatWmZMjldHHzJgxQ5KTk83vfXH62nq/PndZbDabfP7552acP//8s2RmZkp0dHQN3jEAX0dQBcAvPPnkkxIbG2sO5Bo2bFjivpSUFPFG/fr1k0svvdT59fDhw+XMM880Qco777xT5vdkZWVJVFSUyRLpxdvGXReqcmBeHaGhoeJNQkJC6v01P/nkE0lISJAXX3zRnMDQjF95JYinnnqqDBgwwGz/85//lCZNmsizzz4rP/30k1xwwQWVvpbuX/p7/+WXX8qtt97qvH3Xrl3y119/mUzpt99+W+b3arZOHzd9+nQZO3asfPfdd3LZZZfV+H0D8F2U/wHwC5s3b5bu3bsfE1ApPbizaJmPHsB/+OGHzrIgLTeyLF261BzkxcTEmLklJ510kjl7XlpaWprcfvvt5kBRs0EtWrSQCRMmyP79+8sdY25urpx++ukm+NPMWnWdeOKJ5nrr1q0lyqdmzZolN9xwg3mfOo7i95UuX9OM0QknnGDOxut7HDhwoHz22WclHjN//nw55ZRTzDgjIyPN4//+++9qj7cm47bGePzxx5sgS8c5btw4Wb169THPqyWcWg6mQZNef//992W+fllzqrS87KqrrpJmzZqZn59mSjSbkpeXZ8Z3/vnnm8dp9tPaT6xyubLmVGngrs+XmJhoxtO7d2+zj5VVHvnCCy/If//7X2nfvr15bf0ZaFBQEd3fNEh+9dVXnbfpvhYYGCiNGzc2GReLvo/iGZvic6p0DPHx8WZbs1XWeyvr89FMrv4O6OPvuusuk3msKt2nNJiy9vfS+1hF9Gdv/U5XhX7e55577jGvoRmoRo0amWCpPJrJ6tatm/k5awmhfg0AZSFTBcAv6DyquXPnmpKh0vMuivv444/N2XCd73HNNdeY2/TgVumBux7QabCh8yz0DL9mVvQAWgOAwYMHm8cdPnzYPE5L26688kqTmdEDXD2zrme99Ux7WSVoZ511lpnXMW3aNHMgXV3WQaYeRBengYke+D700EMmYCyPBgs6Xg0+77//fhOAahD522+/ycUXX2weo2fsNajs37+/PPzww+agfeLEiSYw0rP++rnV5bj156OZAj0Q1myFlqpphuu4444zY7WCAy3BO++888wB8dNPPy0HDhyQK664okRwVp49e/aY96GBiu4DXbp0MUGENhXR1xsxYoTccsstJoB54IEHpGvXrub7rOuyfra6j2zatEluuukmE6B9/fXXJpjR1yiePVF68K9lZtdee60JaJ577jkTFGzZsqXcrJL+rHS//vPPP83YlJbI6fcfPHjQlCvqz1Xpz8kKTErTz1s/Tw28NIOjr6t69erlfIwGT/r56/6uAaDur5px0t+Tisr4igfl+lnofqNZPX0NDVb0s6wK60SABkRVpfvvmDFjzL5m/T5bgV15n6me5NAM1p133uksW9V9qKwyQgDQs1cA4POmTJliCwoKMpehQ4fa7rnnHtvvv/9uy8vLO+axUVFRtssuu+yY288++2xbaGiobfPmzc7b9uzZY4uOjraNGDHCedtDDz2kaQHbd999d8xzFBUVmesZM2aYx3z99de2zMxM2wknnGBr0qSJbenSpZW+l61bt5rvffTRR22pqam25ORk28yZM219+/Y1t3/77bfmcRMnTjRfH3fccbaCgoISz2Hdp8+l0tLSzPsYPHiw7ciRI2WOWa87duxoGzt2rPM2lZ2dbWvbtq3t5JNPrtNx6+fUsGFD29VXX13iefV5YmNjS9zep08fW9OmTc37Kr4P6PO2bt26xPfrbQ8//LDz6wkTJtgCAwNtCxcuPOY9WO9bf276ffpzLE1/lnqxvPzyy+axn3zyifM23e90P2zQoIEtIyOjxOfTuHFj28GDB52P/fHHH83tP//8c4Wf74033mhLTEx0fn3HHXeY/TIhIcH21ltvmdsOHDhgCwgIsL3yyivOx+m+Xvwz0Z9N6c+k+GP1vscee6zE7foz7N+/v60qbrrpJlvLli2dn6X1cym971v7wbRp08yYdu7cafvmm29s8fHxtrCwMPN1cfqZd+/evcRt+r7GjRtn9qOkpCTb448/bm5fs2aNee5Zs2Y5X6f0z1tfS2/fuHGj+Vp/TuHh4baXXnqpSu8TgH+h/A+AX9Auf5qp0rk7y5cvN2f/9Wy7dhPTDFJl9Oy8Zj+05Kldu3bO25s2bWrOgmtWICMjw9ymZ7e1vEvP9JemmYPi0tPTzRn0devWmfKx6jRq0EyRZhb0rLlmQvQsvGZvrOyCRRtzVDZ/aurUqSY7ct999x0zx8gas3bo0wYD+n4186PZN71oFknLIDVLUrzhgavHrWPUzI5mDKzX1os+RrMm2oxA7d2714xVM1paWlZ8H9DMVUV0/Fo2eMYZZzjn8ZT1WVTHpEmTzHvVcVs0O6IZJc1qapazOO0yVzwLY2WVNFNVEX3cvn37ZP369c6MlGbV9HbdVrqfahxZXqaqqq677rpjXruy8amCggIzt0nfo/VZapZTSzzLK63TsjvdX1q2bGkyS1r2qb+zVck6WnQf0flXWvKn9LX0+Sr6HPQxug906NDBfG2VmlICCKAslP8B8BtaUqcTzXVejAZWOsfmpZdeMgdqehBe0QF3amqqKf3q3LnzMfdp2ZcejGs3QS2x0iBBS8+q4rbbbjOdx7R0zSrPqiotTdO5PVqCp+Vf+v1ldfPTcrOqluBVVBqpAZWqaKK+BomVlWXVdNzW61tzsErTsky1fft2c92xY8djHqM/vyVLllT4c9bguKLPobp0PDoWfb/FWeWC1ngt2qGyOOvzPHToUIWvYwUIGkBpwKH71BNPPGECEi3Ts+7Tz0mD/prSoNuad1V8jJWNT+mJCf2MtbxSSwAtOmdJAx4Nrkt/Tm+88YZ06tTJ7Fvvv/++Cd5r0rVSTwZoyab+7mvpn3a/LC9I1uBdg2Et1yw+Tm16oSdNNmzYYMYEABaCKgB+R+dxaIClFz0w0nkSOsdFMyj1TedRffHFF/LMM8/IRx99dMwBZUX0QL289XeKi4iIEFewslDPP/98uRm1qiwMW9NxW6+v86rKmtNS3bbonqq8rGLxZhNl0aYaGohq0KFzy/TxQ4cONQGQztvS4E2DqmHDhlVrP6vq+KrCyvKU17VPs3YaYBWnAZiVNdRMsc6f0wBJM3LVWYhYs5k6n0pPZGhTFGueYFn0/wOdU6VzxfRS1vuw2s4DgPKNv0AAUEPWwZqWjFnKOnutB6ba6c4qrSpOS/f0IFXLiZQeuGlDjKrQg0Qt/9OmBVpeVN5CqHXNmryv47bKncp7jGY6qhIUuZr1+loqVtHra1OS4pmt4sr6+ZX+Oev7q+znV50yQB3PihUrTFBYPJjR/ab4eF1Bs1UaVGlwpYGv7lOaldIySG04olm6yoKBmpQ4VoWWif7444+m9E+zw6VpOaQGK6WDqtIBnTYe0ce8/vrrply1OrQEU7N3miWsqNRWx6HZyrJOtGhzGs10EVQBKI45VQD8gs63KetMv5b4qOJlfTpnQ8t/Sh/MafCjB4XF25DrHBY9wNKz51b5mZb+WeWFpZU1Bm21rmVJb7/9ttx7773iDvre9ABcD1hLL4RqjVk7/mlgo6VkOheoNC3rqks6B04/Y12cOT8/v9zX13luesCsLcu1ZKz4nCztglcRDXo00NWFXrUTY2nWZ2GtmVV6PymLLnSsHeN0LlHxuUWvvfaaybRoS3pXBlW6f+prWeWA+p40O/Wf//zHfG6VzafSkwdVfW/Vob8PGljdeOONJqgqfdH26lpapxmiiug8PM1evfzyy+Uu2lse7eypgVJZ2SeLlvFqYKrZtLLGqZltLQnULoYAYCFTBcAv3HzzzWZOlDaP0BbZOq9K14LSg08tldIDJYsGD9omWg9CrZIqLR3SM9x6YK4BlLb71nIzPWutB4Ha+MJy9913m/bbOm9IW5Tr82lba51cr4FTWfNZdO6GzuX517/+ZbIKVW0v7SoarOj8Mj3o1LJILY3SeTIaHOrnpgGKHpz/73//My3VdR6Ufmba6EPbjWvQqs+hwUhdjlEzeePHjzdt6nVOjGaWduzYIb/++quZ76LZC6XBoTYV0J+V/gz089cgRsddVkBYnAZtOvdHgx2d/6VZDc1kakmYNnrQeWAatGmgrXOANHDTOT5Ww4XS9Dl0P9Fs5OLFi83+pvuHru2lgYEGs65iBUyakdP3YdGGFbq+l7XuVWVllzq/UH83tDw2Li7OZG1qO89Msz/aNl8DvLJoE5l3333X/CxLNy0pTX/H9PdLlwEo3TSjIpoVLL3mVml6kkSDZx1PeUGy/u7r+7GWUQAAWqoD8AuTJ0+2XXnllbYuXbqYNtbaGr1Dhw62m2++2bZv374Sj123bp1pRR0REWFaKhdvr75kyRLTUlyfIzIy0jZq1CjbnDlzjnk9bV2traObN29uXqtFixbmefbv339MS/XitNW73v7666+X+16s1tvPP/98he+5vFbRZbVUt/z000+2YcOGmfceExNjGzRokO3zzz8v8RhtfX3uueea1t/a2lrbVl9wwQW2P/74o8LxuGLc1menPwNto64trtu3b2+7/PLLbYsWLSrxOG3R3rVrVzPGbt26mRb3pduHq7Lah2/fvt20Vrfad7dr1860LM/NzXU+5t133zW3a5v+4u3VS7dUV7qPXXHFFaZtvu4PPXv2NO+zqp9PeS3Oy6It1PXxxffr2bNnm9uOP/74Yx5f1mei+7S2SNexFn9tfawuOVCa3l/RIYWOJTg42DZ+/PhyH6Ot+fV36pxzzql0PygsLDQ/d71YbfcraqlekdKvoz+bVq1aVfg9I0eONJ9zfn5+hY8D4D8C9B93B3YAAAAA4K2YUwUAAAAAtUBQBQAAAAC1QFAFAAAAALVAUAUAAAAAtUBQBQAAAAC1QFAFAAAAALXA4r8iUlRUJHv27DELMAYEBLh7OAAAAADcRFecyszMlGbNmpmF76uCoErEBFQtW7Z09zAAAAAAeIidO3dKixYtqvRYgioRk6GyPriYmBh3DwcAAACAm2RkZJiEixUjVAVBlYiz5E8DKoIqAAAAAAHVmBZEowoAAAAAqAWCKgAAAACoBYIqAAAAAKgF5lRVUWFhoeTn57t7GHCToKAgCQ4OpuU+AAAAjkFQVQWHDx+WXbt2mZ718F+RkZHStGlTCQ0NdfdQAAAA4EHcGlQ9/fTT8t1338m6deskIiJChg0bJs8++6x07ty5xOPmzp0r//rXv2T+/PkmY9CnTx/5/fffzfeogwcPys033yw///yzWaDrvPPOk1deeUUaNGjgkgyVBlR6QB0fH0+mwg9pMJ2XlyepqamydetW6dixY5UXggMAAIDvc2tQNWvWLLnxxhtl4MCBUlBQIA888ICMGTNG1qxZI1FRUc6A6pRTTpH7779fXnvtNVOCtXz58hIHtZdccons3btXpk6dakr0rrjiCrnmmmvks88+q/UY9fn0oFoDKiuIg//Rn31ISIhs377dBFjh4eHuHhIAAAA8RIDNg2raNBOQkJBggq0RI0aY24YMGSInn3yyPP7442V+z9q1a6Vbt26ycOFCGTBggLntt99+k9NOO81kmJo1a1alBb5iY2MlPT39mHWqcnJyTHaibdu2HEj7OfYFAAAA35dRQWxQHo+qYdKBq7i4OHOdkpJiSv400NLSwMTERDnhhBNk9uzZzu/RTFbDhg2dAZUaPXq0yWTp95YlNzfXfFjFLwAAAABQEx4TVBUVFcltt90mw4cPlx49epjbtmzZYq4feeQRufrqq00Gql+/fnLSSSfJxo0bzX3Jyckm6CpOSwQ1MNP7ypvLpdGndWnZsmWdvz8AAAAAvsljgiqdW7Vq1Sr54osvSgRa6tprrzXzpPr27SsvvfSSaWTx/vvv1/i1dH6WZsWsy86dO13yHlB12vDjhx9+cPcwAAAAAN8Iqm666Sb55ZdfZMaMGdKiRQvn7dq+WumcqeK6du0qO3bsMNtJSUmmTLA4bXqhHQH1vrKEhYWZ+sjiF1+l5ZHaMXHcuHHV/t42bdrIyy+/LO5w+eWXm8BLL9ogQks/dW6dBtNWsF1VH3zwgSkRBQAAAHwuqNIeGRpQff/99zJ9+nTTAKD0Qb02mli/fn2J2zds2CCtW7c220OHDpW0tDRZvHix8359Lj3wHjx4sPi79957z7Sb//PPP2XPnj3iTbTro3Z13LZtm0yePFlGjRolt956q5x++ukmcAYAAADE34MqLfn75JNPTOvz6OhoMwdKL0eOHDH3a5bi7rvvlldffVW++eYb2bRpk/z73/8261pdddVVzqyVHnzrnKsFCxbI33//bQK1f/zjH1Xq/FeTQDA7r8Atl+o2atRFi7/88ku5/vrrTaZKMzal6dpe2tJeu9k1adJEzjnnHHP7yJEjTfvw22+/3Zkxsua36TphxWk2SwNgi3Zi1KySPp/OWdPmIkuWLKn2Z60ZRc02Nm/e3Myl05b7P/74owmwir+X//znP9KzZ0/Thl/nx91www3mvauZM2ea0lEt87Teh74H9fHHH5sGJ7rv6etcfPHFx2Q9AQAAAI9ep+qtt95yHsAXN3HiRFP+pbR5hbay1oN7Lenr3bu3WY+qffv2zsd/+umnJpDSBhbW4r8aiNWFI/mF0u2h38Ud1jw2ViJDq/4j++qrr6RLly5mDtqll15qPkudT2YFSL/++qsJonRh5Y8++sisvzRp0iRzny7KrJ+1rvelAWt1ZGZmymWXXWbWFdNA8MUXXzQt7rW5iAYwtXHiiSeacen4/vnPf5rb9GeuP2/NdGpzEw2q7rnnHnnzzTdN10gN+h566CFnxtNaFFrXINNW/fr5aDB1xx13mP3O+gwAAAAAjw+qqpp5ue+++8ylPNrpzxUL/fpi6Z8GU0qzeZqt0TXArCD2ySefNBm9Rx991Pk9GrBYn6nOxbKyONUNfIr773//a+Y06Wtr6V5taaC4YsUK59caLFo0Y/bEE0/IddddZ4Kq0NBQky3TQLL0+7jyyiud2+3atTOBmWbtNMtlBV4AAACARwdV3igiJMhkjNz12lWlWRkth9T5alab+QsvvNAEWlZQtWzZsmpnoapi37598uCDD5rSO80AFRYWSnZ2trO5iCuCcSvbpqZNm2ba5GtZqK45pvOtNLuprxkZGVnu8+g8PC0FXL58uRw6dMjZAEPHWbo5CgAAAI5asydDmkSHSkJ0uLuH4hEIqqpJD+arU4LnLho8aXBRfF6ZBiM6T+n111832ZuIiIhqP6+W2pXOMGoZXXFa+nfgwAF55ZVXTEMRfU1tKKLlha6wdu1aZ1MTbWKh2S+dN6aZN82w6eLQOudOX6+8oCorK0vGjh1rLlo+Gh8fb4Ip/dpV4wQAAPA1eQVF8szkdfL+31ula9MYmXzr8e4ekkfwiJbqcC0NpnSOlM5l0myUddGMjAZZn3/+uXlcr1695I8//ij3ebR0TrNMxWnwoc1EigdW+tzFabOQW265xcyj6t69uwmq9u/f75L3pp0dV65caebNWdkmzTDpex0yZIh06tTpmC6HZb0PzWpp4PfMM8/I8ccfb0oKaVIBAABQvj1pR+TC/841AZVal5whR/JKHmP5K4IqH6Rrfmk5m2ZrevToUeKiwYhmsdTDDz9sAiy91uyPBivPPvtsiflJ2op99+7dzqBISwdTU1Plueeek82bN8sbb7xhuvEV17FjR9NZT59z/vz5cskll9QoK5abm2sCOH197R741FNPyVlnnWUyUxMmTDCP6dChg8mUaVMMbVKhr/v222+XeB59HzpPSgNIfR9aFtiqVSsTbFnf99NPP5mmFQAAADjWzPUpMu7Vv2TpjjSJCQ8201L0HPvW/VnuHppHIKjyQRo0jR492pT4laZB1aJFi0yjBw2Qvv76axNQaJt0bTCh87Asjz32mCmv006LmqGyWthrAwgNprSphT7+rrvuOub1NajTNujjx483WauEhIRqv4/ffvvNLACtQZE22tDFobWZhLZV1yYaSsegLdU1GNSgUUv5dH5VcdoBUBtX6JwyfR8aEOq1tmXX96/zpzRj9cILL1R7jAAAAL6ssMgmL05ZL1d8sFAOZedLz+ax8ustx0v3ZjHm/k2p9mVs/F2ArbqLH/kgbW6gAYh2x4uJse8gFm14sHXrVjOHR9dygv9iXwAAAP4kNTNXbv1iqczZfMB8femQVvLguG4SHhIk936zQr5ctFNuPamj3H5yJ/GX2KA8nt9xAQAAAEC9mr/lgNz8+VJJycyVyNAgefrcnnJWn+bO+9snRJnrzWSqDIIqAAAAAEZRkU3e/nOzvPD7eimyiXRMaCBvXdpPOiREl3hchwT7mp6bU5lTpQiqAAAAABj3frtCvl68y2yf27e5PHFOjzKXE2ofbw+qtqQeNoFYYODRNUT9EUEVAAAAAMnIyXcGVE+d01MuGtTSrNFalhaNIiU0KFByC4pkd9oRaRlX9tqg/oLufwAAAABk3d5Mc90sNlwuHtyq3IBKBQUGSNsm9nlVm5hXRVAFAAAAQGTt3gxz3bVp1TreOZtVpBBUEVQBAAAAqH5Q5ZhXtZlmFQRVAAAAAKofVB3tAHhY/B1BFQAAAODnCotssn6ffU5V16Yl26eXp3gHQH9HUAUAAAD4ua37syQnv0giQoKkdWP7XKnKWI0q9h/Ok7TsPPFnBFU+6vLLLzcdW0pfNm3aJN7ogw8+kIYNG7p7GAAAAD5d+tc5Kdp09quKqLBg0ylQ+XsJIEGVDzvllFNk7969JS5t27at9vPk5fn3mQcAAABfV935VJb21ryqFP9uVkFQVV02m0hBlnsu+trVEBYWJklJSSUuQUFBMmvWLBk0aJC5v2nTpnLfffdJQUGB8/tGjhwpN910k9x2223SpEkTGTt2rLl91apVcuqpp0qDBg0kMTFRxo8fL/v373d+X1FRkTz33HPSoUMH89ytWrWSJ5980nn/vffeK506dZLIyEhp166d/Pvf/5b8/Hzn/cuXL5dRo0ZJdHS0xMTESP/+/WXRokUyc+ZMueKKKyQ9Pd2ZcXvkkUdq+YMEAABA6aCqWxXnUx3bAfCw+LNgdw/A6xRmi3xl33nq3QWHRYKrVuNant27d8tpp51mygM/+ugjWbdunVx99dUSHh5eIlD58MMP5frrr5e///7bfJ2WliYnnnii/POf/5SXXnpJjhw5YoKkCy64QKZPn24ec//998u7775r7j/uuONMZkyf36LBkpbxNWvWTFauXGleV2+75557zP2XXHKJ9O3bV9566y0T/C1btkxCQkJk2LBh8vLLL8tDDz0k69evN4/VwA4AAACusdax8G+XmmaqUgmq4KN++eWXEsGHZpk0U9SyZUt5/fXXTcanS5cusmfPHhMgadASGGhPXnbs2NFknSxPPPGECXieeuop523vv/++ea4NGzaYjNcrr7xinveyyy4z97dv394EV5YHH3zQud2mTRu566675IsvvnAGVTt27JC7777bjMkagyU2NtaMV7NtAAAAcJ1DWXmSnJFjtrskVTdTZT/hv8nPFwAmqKquoEh7xshdr10NWkqnWR9LVFSU3HjjjTJ06FAToFiGDx8uhw8fll27dpmSPaWld8Vpad6MGTPKzBBt3rzZZLJyc3PlpJNOKnc8X375pbz66qvm8fp6WnKoZX6WO+64w2TCPv74Yxk9erScf/75JjADAABA3Zf+tYyLkOjwkGp9bwdH+d+Og9mSW1AoYcFB4o8IqqpLg5FaluDVFw2idH5TTb+3OA2CzjjjDHn22WePeaxmqbZs2VLh882dO9eU9z366KNmjpZmnjRL9eKLLzofo+WHF198sfz6668yefJkefjhh81jzjnnnBq9BwAAAFRujdWkIql6pX8qPjpMosOCJTO3QLYfyJZOidXLdPkKGlX4ma5du5oAx1as6YXOm9K5TS1atCj3+/r16yerV682ZXsaqBW/aACmpXoRERHyxx9/lPn9c+bMkdatW8u//vUvGTBggHn89u3bj3mclifefvvtMmXKFDn33HNl4sSJ5vbQ0FApLCx0yWcAAACAY+dTVbfzn9Lqp3bODoD+WwJIUOVnbrjhBtm5c6fcfPPNponEjz/+aDJCWnpnzacqi5YNHjx4UC666CJZuHChKeH7/fffTVc+DXa00YXOy9L5UdoAQ++fN2+evPfee+b7NYjSOVOaedL7tAzw+++/dz6/Nr7QjoPa6U+DLQ309HU0CFQazGm2TIM27TiYnZ1dD58WAACA76tpO/XS86o2+3GzCoIqP9O8eXOZNGmSLFiwQHr37i3XXXedXHXVVSWaSJRFO/ZpoKMB1JgxY6Rnz56m5bouyGsFY9oi/c477zQNLzQYuvDCCyUlJcXcd+aZZ5oMlAZOffr0MZkrfbxFu/0dOHBAJkyYYLJV2lVQG2touaDSDoA6Vn3O+Pj4Ek00AAAAUDP5hUXOJhPdahxUNTDXm1P9d62qAFvxOjA/lZGRYeb46DpIxRsnqJycHNm6datZNFezMfBf7AsAAMDXrEvOkFNe/ksahAXLiofHSGDg0WZmVfX76mS59uPF0rN5rPx889HOz74YG5SHTBUAAADg56V/2kq9JgFV6QWAbX6aryGoAgAAAPxUbZpUWFo3jpTgwADJzit0rnflbwiqAAAAAD9V2yYVKiQoUFo1tq+nujnFP+dVEVQBAAAA4u9BVe3Wl2pfrATQHxFUVZG/1ofiKPYBAADgS1Iyc2T/4TwJCBDpnERQVRsEVZXQVt8qLy/P3UOBm1lrY4WEhLh7KAAAAC6bT9W2cZREhgbX6rk6OBYAXrPHnvnyN7X79PxAcHCwREZGSmpqqjmYrmiBXPhuhkoDKl1zS9flsgJtAAAAf59PZRncNk60eeCi7Ydk9Z506d4sVvwJQVUlAgICpGnTpmZ9ou3bt7t7OHAjDaiSkpLcPQwAAACPmk+lWsZFyum9mslPy/fIWzM3y+sX9xN/QlBVBaGhodKxY0dKAP2YZinJUAEAAF+w/3CuvDd7q0xZvc9lmSp1/cj2Jqj6deVeuSP1sLRzzLPyBwRVVaRlf+Hh4e4eBgAAAFAje9OPyH//3CKfL9ghOflF5rZeLWJlcLvGLnn+rk1j5KQuCfLHuhR5Z9YWefb/eom/IKgCAAAAfNiOA9ny1qzN8u3iXZJXaA+merdsKDeP6iAndU0w011c5YZRHUxQ9d3SXXLr6I7SrGGE+AOCKgAAAMAHbUrJlDdnbJYfl++RwiKbs6HETSd2kOM6NHFpMGXp37qRDGkXJ/O2HJR3/9oiD5/RXfwBQRUAAADgQ7T7ngZTk1btFWuZzRGd4uWmUR1kUNu4On/9G0d1kHlbFpgyQ33Nxg3CxNcRVAEAAAA+YMmOQ/LG9E2m/M4ypluiyUz1atGw3sZxXIcmZq7Wil3pMvHvbXLX2M7i6wiqAAAAAC82d/MBeWPGJpm9ab/5WteLGtermdw4qr10SXJNZ7/qCAgIkBtGdpDrPlksH87dJtee0E6iw0PElxFUAQAAAF7qq4U75Z5vV5jt4MAAOadvc9Pa3N3tzMd0S5QOCQ1kU8ph+WTeDjMmXxbo7gEAAAAAqJkF2w6a65Gd42XGXSPl+fN7uz2gUoGBmq2yB1Lvzd4iOfmF4ssIqgAAAAAvXntKndGrmbSMixRPckbvZtKiUYTsP5wnXy3aKb6MoAoAAADwUnvTcsy1J64HFRIUKNeOaGe2dTHgfMcaWb6IoAoAAADwQjabTXan2TNVzRqGiyc6f0BLadIgzIzzx2V7xFcRVAEAAABe6FB2vuQW2LM/SbGeGVSFhwTJP49va7bfnLnJuQixryGoAgAAALzQHkeWSjNBYcFB4qkuGdxKYsKDZUtqlkxZnSy+iKAKAAAA8EJ70635VJ6ZpbLoGlWXD2tjtt+YucmULfoagioAAADAizNVTT209K+4y4e3lYiQIFm1O0P+3GhfpNiXEFQBAAAAbpSRky+nv/aXPPvbump93x5HO3VP7PxXWlxUqFw8uJXZfnPGJvE1BFUAAACAG/25IdVkcL5etKtm7dRjPT+oUlcf305CggJk/taDssixaLGvIKgCAAAA3GjJ9jRzfSArVwqqsZaTs/zPw+dUWbRD4f/1b2G235y5WXwJQRUAAADgRkt3HjLX2r/hQFZeDRpVeEemSl07or0EBohMX5ciq/eki68gqAIAAADcJLegUFbvznB+vS/DHihVRtd7Ss7wrvI/1aZJlJzeq5nZfsuHslUEVQAAAICbrN6TIXnFSv5SMnKr9H0pmTkmsAoODJD46DDxJtePbG+uf125V7akHhZfQFAFAAAAuMnSHfb5VJZ9mVXLVO1xNKlIjAmXIK2n8yJdm8bISV0STLnjO7O2iC8gqAIAAADcZMkO+3wqKy6qaqZqr7Odunc0qSjthlEdzPV3S3c534s3I6gCAAAA3GSZI1M1sE2cuU7JzK3mwr/eM5+quP6tG8mQdnGSX2iTd//cKt6OoAoAAABwA21KsTvtiMlSndwt0dyWklG98j9v6vxX2o2ObNXnC3bIgcNVCyY9FUEVAAAA4AZLHaV/nZNipG2TqGplqry9/E8d16GJ9GoRK0fyC+WDOdvEmxFUAQAAAG6wxFH617dVQ0mIDq9WS3UrU+Wt5X8qICBAbhhpz1ZpUJWZky/eiqAKAAAAcGOmql+rRpIYY2+Lvv9wrmmVXtVMVdNY781UqTHdEqVDQgPJzCmQT+btEG9FUAUAAADUs7yCIlmxK92ZqWrcIMzMrdJ46kBWbqULBu8/nGe2m3vxnCoVGKjZqvbSLj5KWsVFircKdvcAAAAAAH+zLjlDcguKJDYiRNo1iTKlcBpYpWbmmrbqVjlgWZLT7aV/4SGB0jAyRLzdWX2am4u3rbdVHJkqAAAAwE2L/mqWSgMqZZUAplSyALB2DFTNYiOc3+vNggIDvDqgUgRVAAAAgJsW/dX5VBYrO1XZAsB7faCduq8hqAIAAADcmKmyWJmqfZUFVT7SpMKXEFQBAAAA9Ug7/O04mC1aude75dGgKt7KVFVa/udop06mymMQVAEAAABuyFJ1TGggMeFHG00kRFcvU9Xcixf+9TUEVQAAAIAb5lP1bXl0PpVKjLEHSamVZKr2+sDCv76GoAoAAABwx6K/rY+W/hXPVKVkVpyp2mN1/yNT5TEIqgAAAIB6UlBYfNHfkpmqBEejCl2rqkhXAS5DZk6+ZOYWmG0yVZ6DoAoAAACoJ98t2S3ZeYUSFxUqHeIblLivSYMw07yioMgmB7Pzyvz+vY6Ff3XR4Kiw4HoZMypHUAUAAADUg+y8AnlhynqzfcPI9hJYasHbkKBAaRwVarb3ZeRUuPAv7dQ9C0EVAAAAUA/e/XOrmS/VKi5Sxg9tXeZjjrZVz62wSUVz2ql7FIIqAAAAoI6lZOTIO39uNtv3ntJFwoKDynyctQBwajlt1Z0L/9KkwqMQVAEAAAB17KVpG8xcqr6tGsppPZPKfdzRtaoqK/8jU+VJCKoAAACAOrQ+OVO+XLjTbD84rqsEaDeKciRUsfyPduqexa1B1dNPPy0DBw6U6OhoSUhIkLPPPlvWr7dP3rOMHDnS7HjFL9ddd12Jx+zYsUPGjRsnkZGR5nnuvvtuKSiwt5oEAAAA3OmpSWtFO6Rrhqp/67gKH2uV/6WUswCwVf7XjEyVR3FrH8ZZs2bJjTfeaAIrDYIeeOABGTNmjKxZs0aioqKcj7v66qvlsccec36twZOlsLDQBFRJSUkyZ84c2bt3r0yYMEFCQkLkqaeeqvf3BAAAAFj+3JAqszakSkhQgNwztkulj7caVewrY06VzWaTPY6W6s1oVOFR3BpU/fbbbyW+/uCDD0ymafHixTJixIgSQZQGTWWZMmWKCcKmTZsmiYmJ0qdPH3n88cfl3nvvlUceeURCQ+1tKQEAAID6VFhkM1kqNX5IG2nT5GjSoDzORhVllP8dyMqTvIIis5ZVYgzlf57Eo+ZUpafbV5eOiyuZFv3000+lSZMm0qNHD7n//vslOzvbed/cuXOlZ8+eJqCyjB07VjIyMmT16tVlvk5ubq65v/gFAAAAcKVvl+ySdcmZEhMeLDef2KFK35PgCJa0/E8zU2XNp4pvECahwR51GO/3PGYZ5qKiIrnttttk+PDhJniyXHzxxdK6dWtp1qyZrFixwmSgdN7Vd999Z+5PTk4uEVAp62u9r7y5XI8++midvh8AAAD490K/LzoW+r35xI7SyLGob2U0YFL5hTY5lJ0vccW+b4+znTqlf57GY4IqnVu1atUqmT17donbr7nmGue2ZqSaNm0qJ510kmzevFnat29fo9fSbNcdd9zh/FozVS1btqzF6AEAAICj/vfXVjMvqkWjCJkwrOyFfsuiGSgNpA5m5ZlsVfGgauv+LHPdnM5/Hscj8oY33XST/PLLLzJjxgxp0aJFhY8dPHiwud60aZO51rlW+/btK/EY6+vy5mGFhYVJTExMiQsAAADgChoMvT2r8oV+K1+rquS8qhnrUsz1gEo6CMLPgiqtE9WA6vvvv5fp06dL27ZtK/2eZcuWmWvNWKmhQ4fKypUrJSXFvpOpqVOnmkCpW7dudTh6AAAA4FgvTd1oFvrt07KhnN7LfsxaHfGOoCql2ALAh7LyZOG2g2b75G4lp77Az8v/tOTvs88+kx9//NGsVWXNgYqNjZWIiAhT4qf3n3baadK4cWMzp+r22283nQF79eplHqst2DV4Gj9+vDz33HPmOR588EHz3JqRAgAAAOrLhn260O8Os/2vShb6LY/V2a/4AsB/rEsxa111bRojLeOOLi8Ez+DWTNVbb71lOv7pAr+aebIuX375pblf26Frq3QNnLp06SJ33nmnnHfeefLzzz87nyMoKMiUDuq1Zq0uvfRSs05V8XWtAAAAgPrwtGOh31O6J8nANjUr00soI1M1dY09+UCWyjO5NVNVuk1kado8QhcIrox2B5w0aZILRwYAAABUz+yN+2XG+lQJDgyQe0+tfKHfSoMqR6YqJ79Q/tyw32yPIajySB7RqAIAAADw9oV+n3Qs9HvpkNbStgoL/VZW/rfPkan6e9N+OZJfKM1iw6V7MxqseSKCKgAAAKCWvl+6W9buzZDo8GC55aSOtXquhJiSmaqpa+ydrUd3S6zRHC3UPYIqAAAAoBaO5BXKC7/bF/q9aVSHEmtL1URC9NFGFZoBm7bWHlSN6Vb2ckFwP4IqAAAAoBbem71FkjNypHnDCLlsWJtaP5/VUj2voEhmbUiR/YfzTAZscDvWp/JUBFUAAABADaVm5spbM+0L/d5zSmcJD6neQr9l0eeIjQgx25/Ms7dnH9U5QUKCOHT3VPxkAAAAgBp6edoGycorlN4tYuWMXs1c9ryJjnlVM9anmGtaqXs2gioAAACgBjbuy5QvFu402w+c1lUCA13XRMKaV6UrEIUEBcjIzvEue264HkEVAAAAUAPPTF5nGkno2lGD2zV26XNba1Wpoe2bSHS4vRwQnomgCgAAAKimWRtS5Y91KWah3/tqsdBveRIca1UpSv88X7C7BwAAAAB4OpvNJhv2HZYpq5Pl9zXJsmp3hnOh33bxDVz+esUzVSd3JajydARVAAAAQAUWbTsod3+zQrbuz3LeptOnTugUL7eP7lQnr9k2Pspc923VUJJij2at4JkIqgAAAIAKMlT3f7fSBFShwYFyfIcmMqZ7oozumiiNGxzNJrnayE7x8uL5vWVQW9am8gYEVQAAAPDbeVE3fbZE/j2um1wwsGWZj9Eyv40phyUsOFDm3HdinQZSxQUEBMh5/VvUy2uh9mhUAQAAAL9TUFgkj/60WjJzCuQ/UzeYr8vy3dJdzmYR9RVQwfsQVAEAAMDvfLN4l2xxzJFKzsiRqWv2HfOY/MIi+WnZHrN9Xj+yRigfQRUAAAD8Sk5+obzyx0az3bpxpLn+cO62Yx7354ZUOZCVJ00ahMrxHZvU+zjhPQiqAAAA4Fc+nrtd9qbnSLPYcPnwikGmk9+8LQdlw77MEo/7bsluc31m7+YSHMRhM8rH3gEAAAC/kZmTL2/O3GS2bxvdSdo0iZIx3ZLM1x8Vy1alH8mXqWvtJYHn9mvuptHCWxBUAQAAwG+8+9dWOZSdL+3jo5zB0oRhrZ2ZqYycfLM9aeVeySsoks6J0dK9WYxbxwzPR1AFAAAAv3DgcK6899cWs33nmM7Okr6h7RpLx4QGkp1XKN8ttnf7+26J/VoDL21vDlSEoAoAAAB+4Y0ZmyUrr1B6No+VU3vYS/6UBk0ThtqzVR/N3S7bD2TJwm2HRGOps/pQ+ofKEVQBAADA5+1JOyKfzNtutu8a2/mY7NM5/VpIg7Bg02b93m9XmNuO69BEkmLD3TJeeBeCKgAAAPi8D+dsk7zCIhnUNk5GlNEeXQOq8xxzrLQToKJBBaqKoAoAAAA+vy7VV4t2mu1/Hte23DlS44e2cW5HhgbJ2O5HSwSBihBUAQAAwKdpJz/t+KfrUp3YJaHcx3VIaCDDOzQ226f0SJLI0OB6HCW8GUEVAAAAfNrHjrlUFw9uVekivo+d1UP+MbCl3DWmcz2NDr6A8BsAAAA+a9XudFm6I02CAwPkgoEtK318+/gG8sx5veplbPAdZKoAAADgsz6dv91ZzpcQTSc/1A2CKgAAAPik9CP58sPSPWZ7/BD7OlRAXSCoAgAAgE/6bskuOZJfKJ0SG5hW6kBdIagCAACAz7HZbM7Ffi8d0rrcNuqAKxBUAQAAwOfM3XJANqdmmfWmzunLIr6oWwRVAAAA8DlWlkoDqujwEHcPBz6OoAoAAAA+ZV9GjkxZvc9Z+gfUNYIqAAAA+JQvFuyUgiKbDGjdSLo2jXH3cOAHCKoAAADgM/ILi+SzBfbSv/FDyVKhfhBUAQAAwGf8sXaf7MvIlcZRoWbBX6A+EFQBAADAZ3wyb4e5vmBgSwkLDnL3cOAnCKoAAADgEzanHpbZm/aLLkl18aBW7h4O/AhBFQAAAHzCp44s1YmdE6RlXKS7hwM/QlAFAAAAr3ckr1C+WbzTbNNGHfWNoAoAAABe7+fleyQjp0BaxkXIiE7x7h4O/AxBFQAAALzex/PsbdQvGdxaggID3D0c+BmCKgAAAHi15TvTZOXudAkNCpTz+7dw93DghwiqAAAA4BNZqnG9mkrjBmHuHg78EEEVAAAAvFZadp6ZT6VoUAF3IagCAACA1/pm8S7JLSiSbk1jpF+rhu4eDvwUQRUAAAC8UlGRTT5xlP5plipAV/0F3ICgCgAAAF5p9qb9su1AtkSHBctZfZq5ezjwYwRVAAAA8EpWluq8/i0kKizY3cOBHyOoAgAAgNfZk3ZEpq3dZ7YvGdzK3cOBnyOoAgAAgNf5fMEOKbKJDGkXJx0To909HPg5gioAAAB4lbyCIvli4U6zPX5IG3cPByCoAgAAgHeZsiZZUjNzJT46TMZ0T3T3cACCKgAAAHgmm81mLqV9PNfeoOKigS0lJIjDWbgfbVIAAADgVvmFRfLe7K3yx9p9kplTYC6Hc+2X2IgQOaNXU9Phr2fzWNmUcljmbz0oQYEBchENKuAhCKoAAADgNuuTM+XOr5fJqt0ZZd5/MCtPPpy73Vw6JjQwQZYa3TVBmsZG1PNogbIRVAEAAKDeFRQWyTt/bpGXp22Q/EKbCZbuHNNJ2jVpIA3CgyU6PFgahAXLuuRM+WbxLpmyOlk2phx2fv+lQ1q7dfxAcQRVAAAAqFc7D2bLjZ8tkRW70p1Zp6fO6SkJMeHHPDYxJlxO6BQv6UfyZdLKvfLjst3SrGGEDG/fxA0jB8pGUAUAAIB69ejPa0xAFRMeLA+f0V3O7ddcAgICKvwezWRdNKiVuQCehqAKAAAA9Wr5rjRz/e6EATK4XWN3DweoNXpQAgAAoN5o4wldY0p1bx7r7uEALkFQBQAAgHqzLtne5a9lXIRpRAH4AoIqAAAA1GsLddU5McbdQwFchqAKAAAA9R5UdUmKdvdQAJchqAIAAEC90XWnVGeCKvgQgioAAADUi6Iim2zYR6YKvoegCgAAAPVi16Ejkp1XKKFBgdKmSZS7hwO4DEEVAAAA6rXzX/uEBhISxGEofAd7MwAAAOoFTSrgqwiqAAAAUC/WOeZT0aQCvoagCgAAAPW7RhVBFXwMQRUAAADqXG5BoWzdn2W2Kf+DryGoAgAAQJ3blHJYCotsEhMeLEkx4e4eDuBSBFUAAACoxyYVMRIQEODu4QAuRVAFAACAOsd8KvgygioAAADUuXUEVfBhBFUAAACoc6xRBV9GUAUAAIA6lZ6dL8kZOWa7E0EVfBBBFQAAAOrUuuQMc928YYTEhIe4eziAbwVVTz/9tAwcOFCio6MlISFBzj77bFm/fn2Zj7XZbHLqqaeabjE//PBDift27Ngh48aNk8jISPM8d999txQUFNTTuwAAAEBF1u+j9A++za1B1axZs+TGG2+UefPmydSpUyU/P1/GjBkjWVn2heGKe/nll8tsv1lYWGgCqry8PJkzZ458+OGH8sEHH8hDDz1UT+8CAAAAFaFJBXxdsDtf/LfffivxtQZDmmlavHixjBgxwnn7smXL5MUXX5RFixZJ06ZNS3zPlClTZM2aNTJt2jRJTEyUPn36yOOPPy733nuvPPLIIxIaGlpv7wcAAADHop06fJ1HzalKT08313Fxcc7bsrOz5eKLL5Y33nhDkpKSjvmeuXPnSs+ePU1AZRk7dqxkZGTI6tWry3yd3Nxcc3/xCwAAAFxPp3BsKLbwL+CLPCaoKioqkttuu02GDx8uPXr0cN5+++23y7Bhw+Sss84q8/uSk5NLBFTK+lrvK28uV2xsrPPSsmVLl74XAAAA2O1OOyKZuQUSEhQg7eKj3D0cwPfK/4rTuVWrVq2S2bNnO2/76aefZPr06bJ06VKXvtb9998vd9xxh/NrzVQRWAEAANRd6V/7+AYSEuQx5/MBl/KIPfumm26SX375RWbMmCEtWrRw3q4B1ebNm6Vhw4YSHBxsLuq8886TkSNHmm0tCdy3b1+J57O+LqtcUIWFhUlMTEyJCwAAAFyPJhXwB4HurrHVgOr77783AVTbtm1L3H/ffffJihUrTKMK66JeeuklmThxotkeOnSorFy5UlJSUpzfp50ENVDq1q1bPb8jAAAAWDJy8uWz+TvMdo9mse4eDuCb5X9a8vfZZ5/Jjz/+aNaqsuZA6TyniIgIk2kqK9vUqlUrZwCmLdg1eBo/frw899xz5jkefPBB89yakQIAAIB7/PuHVWZOVcu4CPnHIKZawHe5NVP11ltvmY5/WsqnrdKty5dfflnl5wgKCjKlg3qtWatLL71UJkyYII899lidjh0AAADl+37pLvlx2R4JCgyQly/sK9HhIe4eEuCbmSot/3PF97Ru3VomTZrkolEBAACgNnYezJZ//2Bf2uaWEztK/9aN3D0kwPcbVQAAAMA3FBQWya1fLJXDuQUyoHUjuXFUe3cPCahzBFUAAABwmdemb5IlO9IkOixYXrqwjwTTRh1+gL0cAAAALrFo20F5bfpGs/3EOT2kZVyku4cE1AuCKgAAALikffqtXyyTIpvIuX2by1l9mrt7SEC9IagCAABArT1UrH36o2d1d/dwgHpFUAUAAIBa+WHpbvmB9unwYwRVAAAAqFX79Ad/WGW2aZ8Of0VQBQAAgBqhfTpgR1AFAACAGqF9OmDHng8AAIBqW7yd9umAhaAKAAAA1UL7dKAkgioAAABUu336rkO0TwcsBFUAAACoMtqnA8ciqAIAAECV0D4dKBtBFQAAACpF+3SgfARVAAAAqNTrM2ifDpSnVr8NeXl5sn79eikoKKjN0wAAAMCDrdmTIa/+Qft0wKVBVXZ2tlx11VUSGRkp3bt3lx07dpjbb775ZnnmmWdq8pQAAADwUO/8udm0Tz+1RxLt0wFXBVX333+/LF++XGbOnCnh4eHO20ePHi1ffvllTZ4SAAAAHmhP2hH5ZcVes33jqA7uHg7gkYJr8k0//PCDCZ6GDBkiAQEBzts1a7V582ZXjg8AAABu9OGcbVJYZJMh7eKkR/NYdw8H8J1MVWpqqiQkJBxze1ZWVokgCwAAAN5LO/19tsA+zePq49u5eziAbwVVAwYMkF9//dX5tRVI/e9//5OhQ4e6bnQAAABwmy8X7pTMnAJpFx8lozofe0IdQC3K/5566ik59dRTZc2aNabz3yuvvGK258yZI7NmzarJUwIAAMDD1qV6f/ZWs33VcW0lMJBqJMClmarjjjtOli1bZgKqnj17ypQpU0w54Ny5c6V///41eUoAAAB4kN9X75PdaUckLipUzuvXwt3DAXwvU6Xat28v7777rmtHAwAAALez2Wzy7l9bzPalQ1pLeEiQu4cE+F6matKkSfL7778fc7veNnnyZFeMCwAAjz3Y1AvgyxZvPyTLdqZJaHCgjB/S2t3DAXwzqLrvvvuksLDwmNv1j4zeBwCAL9qcelhOfeUvufS9+aYrGuCrrCzVOX2aS3x0mLuHA/hmULVx40bp1q3bMbd36dJFNm3a5IpxAQDgUVbsSpPz354r65Iz5e9NB+Tmz5aYifyAr9l+IEumrNlntv95fFt3Dwfw3aAqNjZWtmyxn8EoTgOqqKgoV4wLAACP8fem/XLRf+fJwaw86ZIULeEhgTJjfao8/NNqSgHhc7Tjn+7WIzvHS8fEaHcPB/DdoOqss86S2267TTZv3lwioLrzzjvlzDPPdOX4AABwq0kr98oVExdKVl6hDGvfWL65fpi8fGFf0SUaP52/Q/7757EnGQFvlZadJ18t2mW2WewXqOOg6rnnnjMZKS33a9u2rbl07dpVGjduLC+88EJNnhIAAI/zybztcuNnSySvsEhO65kkE68YKA3CguWUHkny4Dh7GfzTk9fJLyv2uHuogEvoiYIj+YUmI6snEQDUYUt1Lf/ThX6nTp0qy5cvl4iICOnVq5eMGDGiJk8HAIBH0ZK+16Zvkv9M3WC+vnhwK3n8rB4SVGzxU10MdefBbPlgzja546vlkhQTLgPaxLlx1EDt5BUUyYdztjmzVAGajgVQt+tU6S/amDFjzAUAAF9RVGSTx35ZY4IldcuJHeT2kzuVeYD579O7mcVRp67ZJw/9uFom3Xq8G0YMuMbPy/dISmauJMaEyRm9m7l7OIBvBlWvvvqqXHPNNRIeHm62K3LLLbe4YmwAANT7mfq7vl4uPy23l/M9fEY3uWJ4+d3PNHP14LiuJqjSduua4eLsPrx9sd/LhrUx61MBqIOg6qWXXpJLLrnEBFW6XR79Y0JQBQDwNtl5BXLdJ0vkzw2pEhwYIC9e0FvO6tO80u9LjAk317kFRZJ+JF8aRobWw2gB19JlAnS5gIiQILlkEIv9AnUWVG3durXMbQAAvN2hrDy54oOFsmxnmjmofOvSfjKyc0KVvjc8JEgaRYbIoex82ZueQ1AFr2RlqS4Y0EJiI0PcPRzA61Q7t5ufny/t27eXtWvX1s2IAACoR3vSjsj578w1AVXDyBD59OrBVQ6oSmerkjNy6miUgGus2p0u3y7eJVv3ZznXWNuwL1NmbUg1ywRceRyL/QL10qgiJCREcnL4owEA8H6bUg7LhPfmy570HGkaGy4fXTmoRoudJsWGm9Kpfen8fYRnzxm8+N15kpFTYL6Ojw6TQW3j5MDhXPP12G5J0rpxlJtHCXinGs1CvPHGG+XZZ5+VggL7LyUAAN5GM1Pnvz3HBFTt4qPMor41CaiUtlNXZKrgyVbuTjMBVUhQgGlEkZqZK7+u2Cvzthw09189giwVUK8t1RcuXCh//PGHTJkyRXr27GkWAi7uu+++q/GAAACoa/O2HJArP1go2XmF0rtFrEy8YpDERdV8LpRV/rePoAoezAqeTuqSKC//o4+s2JUuC7YekEXbD0nnpGjp35p11oB6DaoaNmwo5513Xo1fFAAAd3p60loTUB3XoYm8Pb6/NAir8bKNzvI/lUz5HzzY/K32oEpL/rTBil7rBUDtVeuvSFFRkTz//POyYcMGycvLkxNPPFEeeeQRiYiIcMFQAACon3kla/ZmmO2nz+1Z64CqZPmffW4K4GkKCotk8TZ7UDW4HYEU4NY5VU8++aQ88MAD0qBBA2nevLlZBFjnVwEA4E3NKfILbRITHiwtGrnmpCDlf/B0q/ZkSFZeodnvuyTFuHs4gH8HVR999JG8+eab8vvvv8sPP/wgP//8s3z66acmgwUAgDewslTdmsWYBetdwSr/O5iVJ7kFhS55TsCV5m85YK613C8o0DX7PYAaBlU7duyQ0047zfn16NGjzR+kPXv2VOdpAABwm9V70s11t6axLntOXfxXu6mpFEoA4YEWOOZTDW7b2N1DAXxStYIqbaEeHm4/G1d83SpdEBgAAG+wZs/RTJWr6AnGxJgws01bdXiawiKbLGA+FVCnqjU7V1fevvzyyyUszP6HQ+lCwNddd12Jtuq0VAcAeCL9O2aV/3V3YVBlNavYefAIHQDhcdbuzZDMnALTlKVbU+ZTAW4Pqi677LJjbrv00ktdOR4AAOrMrkNHzMFlaFCgdEho4NLnplkFPL2V+oA2jSQ4qFpFSgDqIqiaOHFidR4OAIBHWe0o/euU1EBCXHxw6WyrTqYKHtqkgvlUQN3hdAUAwGvlFxaZkr6qWuNsUuH6EijnAsBkquBBiorNp2KhX6DuEFQBALzS7I37peO/JstHc7dXv516HQZVlP/Bk2xIyZS07HyJCAmSXi1c1/ESQEkEVQAAr/TLCvtyHl8u3Fnt8r/uzV1/cOks/3NTUKUZienr9snUNfvc8vrwTPO32LNU/Vs3cnnJK4AazqkCAMBTLNuZ5sw+HcrKk0ZRoRU+Xhfm3euY79QlKdrl4znaqCLXlCS6amHhqgRTU9Yky8vTNsq65EzRl51730nOzBn829H1qSj9A+oSQRUAwOtk5RbIhn2Zzq/nbjkgp/VsWqX1qdo0jpTo8JA6C6ryCorkUHa+xFUS5LkmmNonr/yx0bTMtugUM/1sCKqgwf38rY4mFe1oUgHUJfLAAACvs2p3uhQV60/x96b9lX7Pmr2OJhUuXp/KEhocKI0dgVRddwAsKCySf360SK77ZLEJqHT9oZtP7CDDO9gPnLekHq7T14d32JyaJfsP50lYcKD0bsl8KqAuEVQBALzO8l320r+YcHvBxdzN9rPxVclU1eXip/W1VtXTk9fJ9HUpEh4SKDeN6iB/3TNK7hzTWXo45opt3Z9Vp68P72Blqfq2aihhwUHuHg7g0wiqAABeZ/lOe9bpkiGtJTBAZMv+LNmbfqRqTSqa1d0Z+/poq/7N4l3y3uytZvulC/rIXWM7O+eTtW9iX9BYPw/AalLB+lRA3SOoAgAPpAHC4u32AyKU36Ti+I5NpGeLhmb7703lZ6ty8gtls6Mkrq7K/4pnquqq/G/pjkPywPcrzfYtJ3WUU0vNI2sbH2Wut6QSVPm7tOw8mbE+xWwPYT4VUOcIqgDAAyeXXzFxofzf23OdgQCOSs3Mld1pR0yXu57NY2VYe/sB45zN5c+r0q54OgdL5zwlRIfV2diS6jCo0pLCaz9ebBphnNwtUW47qeMxj2nXxB5U6eejgST815szN0tmToHpdEnnP6DuEVQBgIfZmHLYBAHaxY2Mw7FWOOZTdYhvYLr4DW/fxHw9Z9MBE5BWOJ+qWUydtjpPig2rk/I/DZA0oErJzJWOCQ3kPxf0lkCteyxFOw7GRtg7GzKvyn/tSTsiH8zZZrbvPbVLmfsKANciqAIADzNldbJzW9dfQknLHaV/vVs2dC5qGhoUaAKZ8gKJ1XvqtvNfXTaq0EDxwR9WmZJHbczx7oQB5baE14CxrSNbRUDuv16ausFkNIe0i5ORneLdPRzALxBUAYCHmbpmn3P7YDZBVWnLdqWXCKoiQoOkX2vHvKpyugDqAsF13aSirhpVaMZBm1NosuH1i/tJG0fQVJ52jnlVW/dTOuqP1idnyrdLdpnt+07tWm+LUAP+jqAKADyIzsVZ7gga1EEyVcdkbaxMVR9Hgwp1tATw2HlVhUU2Wbc3s87bqRefU5WWne+SOU36fp74da3ZfuC0rjKiClmH9vGODoBkqvzS87+vM/MHT+2RJH0cJx4A1D2CKgDwIFPXHs1SKYKqkrYfyJb0I/lmod3OSdHO24c5Fr2du+WAFBVfFdgxt+hIfqFEhAQ5S+Pqis5n0oVWXVECuPNgttzw2RITFJ7bt7lcdVzbKn2fs/yPOVV+Z+G2gzJtbYoEBQaYVvsA6g9BFQB4YOmfdWDMnKqyF/3t3izGBFaWXi0aSlRokMkQWaV+FuvrLk2jzcFmXdJSK2cJYC06AGblFsjVHy0y76d3i1h56tyeVS7jssr/tqQeLrdxB3yP/qyfmbzObF84sKUzYwmgfhBUAYCHyMjJl7mOtuAXDGhprg8QVJWwdIejSUWx0j8VEhQogxxto0u3Vl+87WC9lP4ds1ZVDTNVmmm76+vlpgNkfHSYvDN+gISHBFX5+9s0jjLt5jNyCth//OyEzOLth0xGtqx2+wDqFkEVAHiIWetTJb/QZjINA9s0MrcdolFFmZmqsuaKDO/gmFflaFahQaoGJx/O3W6+HuD4TOuaNa+qpuV/r8/YJJNXJZuOhm9f2t+Z+aoqDcCaxUaYbdqq+4eCwiJ57vf1ZvvK49pIgmMfBFB/CKoAwMNK/3Rh10ZRoWabOVVHaYvo1Y71psoKqoY5mlUs2HpQ/tyQKqe+/JfpmqdZm2tHtJMzezevl3EeLf/LrVE7/f9M3WC2Hz+7u2kXXxPFSwDh+7Tb36aUw9IwMkSuPaG9u4cD+KVgdw8AAGAPGGasSzHbY7olSVykPajKzCmQ/MIiU97m77RVtH5O2gyidePIY+7vkhRtFr/VQHTC+wvMba3iIuXFC3rLwDb20sD6UNO1qjbsy5Tbv1xmti8b2louHNiqxmNo1yRK/tq4nw6AfkC7TL40daPZvmlUB4kpZw0zAHWLv9IA4AHmbz0gmbkF0qRBmPRt2dAEDlZPBZpV2C1zlP7p+lRlNW0IDAyQoe3sXQDVxYNbyeRbj6/XgKp4+V915lSlZeeZxhRZeYVmwdYHT+9WqzG0s9qqU/7n83QdM93XmjeMkPFDW7t7OIDfIlMFAB5gymp76d/orgkmOFCNIkNNowFdAJg5ElJsfaryF/C9fmR7k9m7aHArGdU5QdwhKTasWt3/dD7MzZ8vNe3i9cD4zUv61zozSfmff9Bg/M0Zm8z2HSd3krDgqjc0AeBaBFUA4AGtkKc51qca0z3RebvOqzJBFZmqEkGVZqrK06N5rPx3wgBxpyRHk4iUzBzTyc8Kksvz7G/rTKmedm17d8IAU8JYW1ZL/h0Hs03QFkz5qE96a+Zm0+VRS1/P7ls/cwYBlI3/ZQHAzVbtzpC96TkSGRrkbLagrHlVBFU6tyxfNjmyLromlSdLiA4zzTG0k6NmGSvy8/I98u5fW832C+f3lm7NXNP2Xbv/hYcEmjHsOnTEJc8Jz7In7YhMnLPNbN97Spc6X4MNQMUIqgDAzaasSTbXJ3SKL7EekZWxYE6VyIpd6aLr2Gp5nK7d5Mm0dK9xVOUlgAcO58pDP64y2zeMbC/jejV12Rg0O6brVakt+ykB9EUvT9tgGrcMbhsnIzvHu3s4gN8jqAIAD2qlXtzRtur54u+0ZbQaUqwRhSez5lVV1AHwiV/XyqHsfFO6dfvJnVw+hqPzqmhW4Wu0U6QuF6DuPbVLmY1bANQvgioAcKMdB7JlXXKmKd05sUvJxgpxUfbWyAezqr/ekS9JzcyVX5bvNdve0t2ssg6AM9enyPdLd5sOj8+c16tOWua3a0IHQF/13G/rpcgmckr3JOnXqn4WtQZQMYIqAPCA0r9BbeKkoWMOlSXOUUJ2MNu/M1WfL9gheYVFZsHfshb99UTOtarKKP/Lyi2Qf31vL/u7YnjbOntPdAD0TQu3HTSNbfREzN2ndHb3cAA4EFQBgAeW/hXPVPnznCqdM/LxvO1m+4rhbcRbVJSpemHKetmddkRaNIqQO8e4vuyvdAfArWSqfKpT6LOT15ntCwa0lPaO9cgAuB9BFQC4iXb107PO5QVVuk6V0rbq/mryqr2m/E876p3aw3WNHOpaYqw9qPpjbYq8Mm2jbHMENkt3HDKLtaqnzukpkaF1t7KJtQDwvoxcOZxbUGevg/ozbW2KLNp+yHR2vG10R3cPB0AxrFMFAG4yfV2KmRfRtWmMtIyLPOZ+q4OcP2eqJv5tD0AuHdJaQoO95zzgwDZxEh0ebALil6ZtMBddXys9O890MTy3X3MZ0aluO7bFRoRIkwahsv9wnmxNzZKeFSyaDM+n640995s9S3Xl8LbOElMAnsGtf6GefvppGThwoERHR0tCQoKcffbZsn79+hKPufbaa6V9+/YSEREh8fHxctZZZ8m6dfb/VCw7duyQcePGSWRkpHmeu+++WwoKOCsHwLNNdcynGlNGlko1shpVmANxm/gbzeos25kmoUGBcvHgVuJNtPRuzn0nyovn9zbBkzak0MWLtx3IlsZRofLvcd3qbRyKture77slu2VjymFpGBki157Q3t3DAeBJQdWsWbPkxhtvlHnz5snUqVMlPz9fxowZI1lZR+u/+/fvLxMnTpS1a9fK77//bg4s9DGFhYXmfr3WgCovL0/mzJkjH374oXzwwQfy0EMPufGdAUDFcvIL5c8N+8st/Su+TpXOK8rKs/+f50+sMrkzejeTJg08e22qskSHh8h5/VvIR1cOkvkPjJZHz+xuAujXLurrbJdf15wdAGmr7vX/X2i2U900qoPJQgLwLG4t//vtt99KfK3BkGaaFi9eLCNGjDC3XXPNNc7727RpI0888YT07t1btm3bZjJYU6ZMkTVr1si0adMkMTFR+vTpI48//rjce++98sgjj0hoaP384QKA6pi9cb8cyS80i9l2bxZT5mN0vo3OncjJLzIlgA3C/KdiW9d3+nXFXq9rUFEeXbD4smFtzKU+WR0AaVbh3T6cs032pudIs9hwUwoLwPN4VIF6enq6uY6Liyvzfs1gadaqbdu20rJlS3Pb3LlzpWfPniagsowdO1YyMjJk9erVZT5Pbm6uub/4BQDc0Upds1QVLdwZ52hWoU0t/Mmn83dIQZFNBrZpJD2aMxeopij/837p2fnyxoxNZvuOMZ0lPCTI3UMC4MlBVVFRkdx2220yfPhw6dGjR4n73nzzTWnQoIG5TJ482ZQKWhmo5OTkEgGVsr7W+8qbyxUbG+u8WAEaANSHwiKb6QpXUemfxSoT03lV/iK3oFA+m29vo375sLbuHo5XszoAaqMKf5yX5wve+3urZOQUSOfEaDmnb3N3DweApwdVOrdq1apV8sUXXxxz3yWXXCJLly41c7A6deokF1xwgeTklL1KfVXcf//9JitmXXbu3FnL0QNA9RowaFe4mPBgGdS27Mx86XlVBw/7T1D1y/K9pmNd09hwGdO94qATFWsVFymaCNU5efqZwvs6/n2xYIfZvunEDmbBXwCeySOCqptuukl++eUXmTFjhrRo0eKY+zWb1LFjRzPP6ptvvjHd/77//ntzX1JSkuzbZ18802J9rfeVJSwsTGJiYkpcgIroGV6dk6AZBqC2pjgW/D2xS4KEBAVWKag65CeZKv1dsxpU6NyRyj4fVEzb0FsLEe88lO3u4aAGyy6kZOaajpFju5d9TAPAMwS6+4+nBlQaIE2fPt3MlarK9+hF50WpoUOHysqVKyUlxV5Ko7Q8UAOlbt3qp2UtfN+M9Sky6oWZcvPnSyihQa3o/jNltTWfqvKDpEZ+Nqdq8fZDsnJ3uoQFB8pFg7yrjbqnatnIvgbazoMEVd7mc0eW6v8GtPCqddoAfxTo7pK/Tz75RD777DOzVpXOgdLLkSNHzP1btmwx85+0G6CuRaUt088//3yzZtVpp51mHqPt1TV4Gj9+vCxfvty0XX/wwQfNc2tGCnCFuZsPmOtJK5PNWiFATW1KOWzWKtK1l07oXPnir87yPz8JqiY6slRn92nufO+onRZxEeZ61yH731Z4h91pR2TmhlSz/Y+BnGAAPJ1bg6q33nrLzGkaOXKkNG3a1Hn58ssvzf3h4eHy119/mQCqQ4cOcuGFF5rgS4Mrbb2ugoKCTOmgXmvW6tJLL5UJEybIY4895s63Bh+jCy5aHvl5texJ4+AEtSv9G9ahcZVapHtLUPWfKevlxBdmypIdh2r8HHvTj8hvq+xZvMt9oI26p2WqdlH+51W+XLhTtDBiWPvGzi6OADyXWxc9qayMqlmzZjJp0qRKn6d169ZVehxQm+yCatIg1Ez2vvfbFWZBz4paYQNlmeoIqsZUofTPm+ZUfbVolyRn5Mil/5sv74zvL8d3rDwLV9on87abeYtD2sVJ16bMdXWVlnFW+R8ng7ypQcVXC+1NtCiDBbwDBbpAJbLzCpxlM3qwqHM9/tq4Xz6Zb691B6qzoO2ynWlme3RXe7a9qnOqtFugpzqSV2gCKpWdVyhXfrBQJq20L9xbVTn52kbd/jtFG3XXatnIXv5HowrPoieWdQ5hWhknTGauTzW/U3pShQ6YgHcgqAIqsTkly1xr96X+rePk3lO6mK+f+nWtbNtvvw+oimlr7VmqPi0bSoKjI1tlGjdwZKo8OKjaftD+e6At4sf1bCr5hTa56bMlzlbQVfHTsj1yKDtfmjeMqHTtLtQsU6Vly3Qw9Rzvzd4q5701R8a+/Kes3ZtRdoOK/i0kLJjFfgFvQFAFVGJjSqa57pBgX0Tz8mFtTHnSkfxCuevr5RykoMqmrHaU/lXjzLOVqUo7ku+x+5p1ckHnfbx6UV+5aFBL0aHe991K+e+fm6t0xt5qUHHZsNasxeNiiTHhEhIUYIJdK6MI99K5h89MXme292XkygVvz5U5m/Y7g1/tOKv+MbClW8cJoOoIqoAqNqnomGgPqgIDA+T5/+ttmgws2n5IPpu/3c0jhDc4nFvg7CI5phqZmIaRIeZap6CWVSbkCbSboWrTJMoERE+d01OuO6G9ue2pSeuOOQtf2vytB81jIkKC5MIBzB9xNf2ZNGvoKAGkrbrbpWfny82fLZWCIpuM7Z5oFgDPzC2QyyYukJ+W75GvFu00JyX05F27ePvfHQCej6AKqGKTio4J0SXKaW4/uZPZ/sIxmRju8fvqZDn3zb9lxS77XCVPNWt9quQVFkm7JlHSvhoHSrr4bWxEiEc3q7AyVa0b2zuUaQOX+07t4gwev1uyq8Lv/+Bve5bqnH7NJdYRRMK1WKvKM2hW9q5vlpt26a0bR8oL5/c2TY+sstlbPl8q7/65xTyWBhWAdyGoAqoYVFnlf5Zz+jY3Z4BX78mQzalHW66jfn29aKcs2ZEmV3+0SFIyPbe0acoaa8HfxGp3jTzaVj1fPNG2A1b5n/3A3aLzQdSPy/aUW7qobb6tz+aKYbRRrystHWtV7WStKrea+Pc20wFU16l74+J+Eh0eIuEhQfLaRX1NabnKyiuURpEhMrZ71TqEAvAMBFVAJR3JtjsOGDuWCqr0QPe4Dk3M9s/L97hlfNCSuHznvITrP1kieQVF4mnyC4tkxjr7HImadPLSAyxPXqtq2/7sEpkqy8jOCaZ8MSUzV+Zsts8XKe3judtNqZP+LnVMPJoNhmu1sNaqIlPlNst3psnTk9ea7QdP7yo9msc679Oy8ofP6CYPnNZFggMD5Krj2ppgC4D3IKgCKrB1f5Y54NOuZvHRYcfcf2bvZs6gqrJ111A30o8czd5oe2JdnNnTLNh6UDJyCsw6Z31aNqr298dFhXlsUFW8nXrbUkFVaHCgnN6rqdn+fsnuMpcrsLqcWWfpUcdrVdFWvUy5BYWyYV9mnfw/rs+pjSdu+HSJKfE7rWeSjB/S+pjHaQb7mhHtZfVjY+WmEzu6fBwA6hZBFVClJhXRZZZsadZBDxw3p2bJmkom46NuZOTYg6q7xnQS/RHpWkfWekeeYspqe3nbSV0Sa9TZLi7Kc+dUWe3Udd5XI0eZYnHn9LWXAP62OtkEUcX9sHSPCTZ1bsmJXaq2bhdqt1aVteYeSnry17Uy5qU/5Y+19oyysetnkW2fiyRPEzm0QuRIskhRyX24IkVFNvlt1V454/XZcsXEhWYeVau4SHn63F4VlgDTQh3wTsHuHgDgyTbtyyyz9M+i9fAndk4wB4w/L98r3ZsdLedA/WaqzurT3ByoPP/7enn4p1XSOamBWVfM3fQstc6hUDVdxNMKVjwxU2U1qWjTuOR8Kku/Vg1N0LT9QLZpKX923+bOz+WDOVvN9oShbUz5E+o+U6VZRc3KcOBe0vwtB831wm0HZbTVnXP1UyIH5h374LDGImEJIuEJImHx9mvr4rj9710B8sysTFm5z16OHBkaJJcMbiXXntDe2XjGSQO13P0iOSkiuSkiOVoqq98XIBIQ6LjW3w/HxRmQFf+62G1VfqzN3lZUrAvgAaI7iUTbu8d6G4IqoAKbUstuUlHcGb2bOYKqPXLvKZ2r3YQANacHhzn59oOWmIgQuWFke1m9J10mrUyWaz9eIj/eNNwsJutO2shkT3qOaRc+3DEHr7riIj04qCrWTr0s+vtwdp/m8sofG+X7pbudQdWczQdkw77D5mDz/AH2bBbqji5ervugrq+3Jy3HrCkGO52HaTUb0hJAp8aDRILCRXJTHQGPBjs2kdwD9kuGfX5UWYZrWXiiyIHGsZIb3kYaJ3aRsIYdRDYViBzZe/SSk+x4XgBG76dFut8n3oigCn5Pu49pxumYs4da/rev8qBKy5aiQoNMaYd2oevfuvpzZlC7LJXGsdFhwfZM1f/1li2pWbIuOVPG/2++fHXdUGnS4Nj5cPVliiNLdUKn+BpPPD/a/S/P49upl0UDKQ2q/tqYajo0JkSHmy5oVofAmHDaqNc1/d3QDoAayGpbdYKqknNndc0opZ+P04BXSj6wqFAk74A9wLIuzoDr6G3JKTskynZAooOOSOPgdJGC5SK79VLRKAJEwpo4sl1NRAKCj2aQbEWlskpS8mvnPLDiXxd7bPGvSzy2jEzWMcOq45OE5c1h4+Sk/4rw3q6XBFXwa9rY4B//nStdkmLkp5uGl8gyacc2/WOrKupKFhEaZNpk/7Bsj8lWEVTVnwxHUKUH5Vb5WFRYsLx/+UA5/+25smV/lkx4b4F8fs2QMoPm+mCV/uk+UlNWUOWJc6qs35HS7dSL0wP4vq0aytIdafLTsj0ypluS/LHO/rlcRoOKel2rygRVNKsoYX2x7JSeHMvKLTD/jxwjMOhomV859MTB+OkLTMv06bf0lhYh+0Sytooc3iJyeKtIYIhIRFOR8KRi10kioY3tzw/AaxFUwa9LPu7/boXpxrRyd7op0yre4lZbqevZS81CNYsNr/C5zuzTzARVv6zYK/8+vVuNmhGg5pmq0gFTs4YR8sk/B5vAShuIXPXBQvn4qsEmAK5PmhFYuzfD7A+1acRgzak6cNjzgiqdK1VZpspa102Dqh+W7Za96TnmBLVm76qzEDJc1AHwIM0qituQnHnM2oS9Wzas9vNoY4pnf1tnti8Z0kpaJGp32GYicX1dNlYAnovuf/Bb//1zc4lSj59KrTVVvPSvsnlSx3WINwf2+w/nyrwtB+poxCgvqIqJCC4zO/LRlYNMO/xF2w/JdZ8srtc1rFbuSpd7v11htge2aVRmZ7zqzIfxxExVRe3USzu9VzOz/s6q3Rnyybzt5rbLh5Olqk8tHB0AyVSVpKXCxZWYV1UNk1btNft3g7BguWlUBxeNDoC3IKiCX9qSelhenb7J2WhCaemenmksfrZSta9gPpVF26rr2iNKy5vg3kyVpVuzGJl4xUAzQX/WhlS5/ctlUljsZ1wXVu1Ol39+uMi0UdZmDJq0vOq4drV6Tisgy87TxhyF4i3t1EuXMI7sHG+2cwuKpF2TKDmho/1r1A8WAC6bFUR1dpR5W0tpVIeWi7/w+3qzffXx7aSxG+dxAnAPgir4HW3lfP93K03WYkSneHn+/3pJdHiwKUnSdrrHrFGVUP58quKs4Gzyqr31mhHxZxlH7GvGVDRfStuqvz2+v4QEBcivK/fKv75fWScLfGqAd81Hi+T012bLtLX7TDB1bt/mMu2OE2o1n0ppEw4dv6c1q6isnXp5a1ZZc6loo16/tFGF2ulBa1UdysozpdbuovOndjiCTGuh6o01yFR9uXCn6YSpC3z/8/i2Lh8nAM9HUAW/8/WiXTJ/60EJDwmUJ8/uYTqyndrDnmX6sVgJ4NGgqmpzPga3bSwJ0WFmMdM/N6TW0ehRnUyVRefuvPKPvibQ+WLhTnlm8rpqBVY6Nyo92/5a5Xlp6gbT6U9fQ+cPTb3jBPnPhX2knQvmDGn5aSMPbKu+dX/F7dRLO6lrgilB0zmK5/Wnjbq75lTpPqTBhCf4x3/nyQnPzzTZXc3y1jfr/3ntEDq4XeNjOwBWgS5qrd0t1c0ndiy7yQUAn0dQBb+SmpkrT06yry1yx8mdnAcZZ/a2r50zaaU9y6QlYta6JR0Tq3ZQrM0IxjnOdP68ghLA+p1TVXlnv9N6NpWnz+1ptt/5c4u8OXNzlTtEjnphppz/zhxT4lMWPUj9YuEOs/2/ywbISxf2cXkDBk/sAGhlGCprUmHRExi/3zZCptxxgpl3gvqlXTKtExCeMK9K15mzOu9pdlezvFd/VL/B1frkDHPdJSnaeQLN6gBYVbo8gP5t0UzgRYNa1dlYAXg2gir4hYycfJmzab/c9fVycyDevVmMXDn8aInG0PaNzZnKtOx8mb0p1WQmNLjSuVLWPITqlABqG22dxA/PyFRZLhzYSh4c19VsP//7evnY0TChPBpcP/TjKtMFUs9ea4lPWT6Ys80sQtyrRayM6lzzLn8V8cxMVeXt1EvTs/gEVO4vAdzlAR0A96Xnmmv9f/bsPs1Mllf/79TgSv+vLj7Hta6sT7afPOuUGG3mBVpr2lV1XpWWL77tOEFz58mdzXsB4J/47YfP0bOfy3emyUdzt8kdXy2T0f+ZJb0fnSIX/2++aVagf7ifObeXBAcFlsgyWfX02mjC2aQivkG12qP3bdnQlDdpQwFrHR54TlCl/nl8O7n5RHtnLg2YflxW/oqcn83fblrtW16etvGYM9j69Ydz7AvZXn9C+0o7RdZUXAPPC6qq2k4dnrVWladkqvak2wM7LQd9+R99ZcrtJ5jgSn+Fvlm8S75bWuFquS5tUqGZKtXJUZlQ1Q6Ab87cJJm5BdK1aYyc6TipBsA/cboQXk3PZG49kGWCKL0s25Uua/dkSF4ZZVoa7OjaI//Xv4X0bHF0PSrLWX2amYyDzotp5ThIrOp8KoseUGu26q2Zm01wpm2kUQ/lf+HVW9hXSz914eAP526XO75abjInJ3Ut2UziwOFck81Smt36aO52M6H9/dlb5eaTOjof9/mCHWYc2s1uTPe6Wwk+zpGp0jPj3tZOHZ7Dk9aq2usIqprGRjiXr9DgSgOUpyevk2cmr5Ux3ROr/ftdk3bqnZxBVbTp2mmdWKvInrQj5v8Qdc8pnWm8Avg5gip4nR0HsuXLRTtk+c50Wb4rTTJzjq19bxgZIr1bNDRBVJ+WsdKrRUNnWUd5+rRsKK3iIs2B88dzt9UoqFJnOoKqmetTTdlhXR4Q+DsNjKqbqbKC34fP6G6ainy/dLfc8OkS+fDKQTLEMVFdPffbenO/HuBdPqyNJMSEyy2fLzXzsS4e3Mq0TNYS0f/9tdU8/poR7ep00WerZfnBGs6p0hMQrjzoq047dXiOlh60VtWeNHtQ3rRhycXVrxjeVr5ctFO2pGbJK9M2mgXV64KeONG1BYv/X9+xGpmql6dtMP8HDG4bJyM7sTwA4O8o/4PXufPrZfLGjM0ye9N+E1CFBQfKgNaN5Krj2sqrF/WVP+8eJUv/fbI5SNaMxIldEisNqKwDbat845Cj01tVm1QUp2UkesZVs2W/r0quwTtEXQdVSgOM5/6vl4zummDWTdLuYyt2pZn7lu44ZA7q1ONndTeloqf3bCo9msfI4dwCeX2GfY2zH5btNtka7fp4Tj97s5O6Yi0AXLz8T4P2KyYukJs/X1rh/JNNKZnS57EpZikBd7VTh2do4cxUZXtMpqqZI1Nl0XlJetJDafVATRfjrYzVJENPplkd+6wlNKzF38ujbde1RFHde2qXOiv7BeA9CKrgVbTkaOkO+4Gvnr389ZbjZNWjY+Wb64eZrzUoatU4ssZ/4M7sU7JcT4Oj6ioenP28Ym+NxoG6m1NVXEhQoLx+cT8Z0i7OBEuXvb/AHMA99ONqc/95/VrIgDZxziDsvlPsTS4+mbfddL57e5Z9grquSxMWHCR1qVGpoErbOF85caHMWJ9qFq7W7mnleeWPTSbr9u3iXZKZU3Fr+Lpqpw7PmlO169CROlmvrTr2lpOpspZBGNMt0TSLeeSn1XUy1g1W6Z9j0V/79tEOgPp/Qnm0NFjPY4ztnij9WjVy+dgAeB+CKrhFTn6hfLlwh8xYl+Isv6iKZTvTTCe2xJgwuXJ4G+neLNYcGLuK/nG1JiwHBwbUeAK+1QXw7037TYkJXE/bm2c5OizWNKiy2nz/77KB0rtFrMlQnvn6bFm5O90sCH3fqV1KPPa4jk3k+I5NJL/QJpdPXGjKk2LCg+uljfLROVX5phnLtR8vlkXbDznv1+xZWQee2qHvV0eLf82eahDmjnbq8Aw6t1RpwKDdTt1pT3pOmZkqi54o00oEneM0uQ6y/lamyvo/XzWMDJX4aHtlQ3nzqnSZBWtNurvHdnb5uAB4J4Iq1LuCwiIzh+Xeb1fKFR8slAFPTJPhz0yX6z5eLO/M2lzhmfTF2w+aa80e1FW5hZWt0jPwNQ3Y2jaJkp7NY81Z1kmUANZp6V9V16mqiDaq+OCKQWZehbZGV3ee3Ml5cFXcvad0KdFOfMLQNhJdD/PmGkXZX0NPQujcrr827pfI0CD534QBEhESJCt2pZvulqXp75SeUbfme01Zney2dupwPz2JYO3X7p5X5WxUUUamymqqcd0J7c32E7+sMdlZV1pfqkmFpaIOgHri4tnf1pltbXrUwVEuCAAEVahX+gfpkZ9Xy/R1KeYMZPv4KNM+V0stfludbDo+VbQo68Jt9jPzA1vXXbnFJYNam0V8bx/dqVbP4ywBXMZCwHVZ+hcdFuySBhFaXvfxVYOlf+tGMrprolw6pHWZj+vRPNaZidR9+PLhbaQ+NI6yHwgfyMqT31fvk9CgQHl3wgAZ3S1RLhlsz5S9Nr1ktkoPWr9dYp/38cBp9tJFbaCima7aop26DzSrcGMHQC3ltjJlVve/slw/sr00bxhhslraAMhV9PdE154rnakqOa/q2KBKf38WbD1o5n3dVsu/EQB8C0EV6pV2Svtk3g4TSL18YR/5486RsuLhMfLFNUNkwlD7Qewf5cwN0azPEke5kzXPpS7ERobIGxf3M4FVbVjfv2DbQdN6F3XUTr2WWarikmLD5dvrh8n/LhtQYh2z0rQssG+rhnLPKV2q1ATFFbSjpUWDyDcu6SfDOzQxX189op05yNOypHlb7Nlc9e6fW02ponYnu2JYG0mKCTdlX3M2HajVWGin7iNt1d2YqbLWqIoKDTIltBVl1v59uv2EgHbetMpOa8uaMxUSFGAqC4o72gGwZPmfNoOxslTaEbRZw/KDQQD+h6AKVbYvI0cWbTto/qjpQVV1TVq5V56ctNZs/+u0rnJqT3vQoaVT2spaV6PXhIP+IdtVxh97LcXQRRb1j3DpM4ueSP/gDnIEf7/SsMIrgqqq0jPn398w3HScrC96cKnzYfSExH8u6C0ndzu6rlZiTLhcOKCl2X5t+kZzrXP5dA0tdeOoDqbRhq75o36vZQngNseBLe3UvXwBYDd2ADzapEL36YozzWO7J5m5jNq+/PFf1rjk9a3SPl3gvXSZt9W4ovScqp+W7zHrWul8yxtG2ssSAcDCOlWoEj2jd+orf5Vo56x/WLSVtB7Q6XVCsevEYl9rq1qdC3Xbl8vM9102tHWZB6OaIdLSKy3x0xKL0uVXGtCpfq0bVZhF8CRn9G5qMlX6x1izCXAd7WanYiP857+xz68eYpYR6NYs5pj7rhvZ3gRROqlff9/0d+hIfqH0ahFrDkjVmG5JZhHjqWv2yZPn2GpcNmllC2in7p1axkU4OwC6O1PVNLbs+VRlrSt3yst/yrS1KTJjfYqM6pzgmkV/i3X+s1hrVlnZLJ1zqQHdi1Pti4HrPC9taAEAxfnP0Qhq5cdlu01ApSVGehymk/n14E4vm1MrLsfQP0gFRUXmj5KuCfTQGd3LPTM5snNCuUGVNZ9qQOu6K/1zNc3GPfLzGtNNTif2ly4zgfvaqXtz2VZ52TNtAa/ra2m759V7MsztN4zs4Px9G9wuznxeOi9LSwUHta3Z7xLt1L2bJ2Wqyuv8V5oub3HF8Dby7l9b5bGf18iw9o1rtYyB1U69cxlVD1YHwNTMXDOvqm+rRvLZ/O1mDpqeKLxyeP1lqAF4D+843Q+30gm9n86zlxHdM7azrH3sFFn+8BiZdscI+eyfg+WlC3vL/ad2Mdmn03s1NQdqGjxoZzKlZ/o0CNMz5ro4b0Vnx0d2jne2Ii89md7KVA1o4z1rguh8G/3jr3QtIXjGwr++Sif166+XzqvSEx56IKpr/Vi0zOmkLgm1LgGknbp3s4LhHQezXdK0pC46/5XllpM6mmBHT1C9N3urSzJVncvIVBXvAKiLAOvfMG0Co24d3VEiHH/bAKA4MlWo1PJd6bJmb4bJUumZcD3rrQeyeqmsnaz+MUrJyDFZLi1ZigyteJfr1jTGnAlMycw1HZaO7xjvLMPQ7k8akPVp2VC8iXYB1PbXWgJ484lHswaoHX/MVFXlYFn3tx8cHSd13ofOpSpuTPck+W7pbhNUPTiua432R2tOFeV/3klL7rQ5hJbQbk7JKrOc1N1rVJVF59/qCbw7vlour0/fJOf0bV5h58CK1rjTNebKy1RZHQD/3nRANqZkyv/+OmKyu3qy8ALH3EUAKI1MFSr16bzt5vr0nk2rPSldS//axTcw3foqC6iUHuBZtfIz1qUek6Xq3izGzNHyJnoQq+2vddKzdXYUtZfuaMdMUFXSTSd2cC5XYLV+L+6ETvESHhJo5tPoyZKasFpxtyao8kr6/2yXpvZAal1yzfaB2tqbVv1MldJAakDrRpKdVyhPTbJ34quubfuzzELY2vRIy2bLYs21mr/1oLz75xazfeeYTi5dbB6Ab+F/B1SaDfh5hf2s98WOtXDqmlUCOHNDivO2RV44n8qiB/3We6IE0De6/3kyzR5Pv2ukfHf98DIPALV0aYQjA6zrXVWXzo20SrcqmuMFz9bVkaFx14mevY5MVXUzTRoQPnKmzsu1/386b0v1lwdY7+j81zEx+phMbunyP11UOyuv0CzmflqP2i2zAcC3EVShQt8v2WXmQ2nduXbmqw/DOzaR4MAAU55hzd1Y5FyfynvmUxVnZQw0QC2+OCtqjvK/8unZd+2mWVGLajWlBvOqdM21Ipu2eA+U+HpaowuuZ2Wq1tYwW1kbGTn5pjRcNatmpspagPviQfaTfI/8tFoKCouq9f3Ld6aZ64qW5rAWALbce0qXcgMwAFAEVai4QcV8e4OKS4a0qre5QDHhIc7gSbsA6h9gq0RFyz680UldE0zjDi2bWub4g47a0f1Ckamq2f6o8xM1S1HdxVS1uYHVQY75gd6rixszVVbnPz0hUpWy8LLcNaazWRBbx/+Jo0S9KnR+ri5Ar6w5u2XRkxI6v1cd16GJHOdYlgAAykNQhXJpdmhjymGJCAmSs/s2r9fX1tbqaub6FFmy/ZBockfnb+jaV95IDxxGd7V3YdOGFag9MlU1py2jh7SLq1EXQCuoakXpn1fTOUMaE2vb8P2Hcz12jary6PxeDazUf6ZuMItdV8VjP68267dpl9rTetoztuU5rWdTsx7j/ad1qfE4AfgPgipU2qBCu4lp9qg+Wc0qdCFTba+u6qv8sK7o56h+WbFXCrV+CrVCUFU7VglgdedVWWsbMZ/Ku2nDn9aOn+H6es5WOdeoKqdJRFVdNKiVaV6kXQx1bbbK6KLBur9rlvbxs3pUmmnVuVtL/n2ydG8WW6txAvAPBFUok7ZAn7Qy2Vn6V990knCz2HDJLSiSzxwliAPbeF+TiuJGdIo3bYz1zPD8rdWfXI2jNCjVdZgUQVXNjOlmD6qW7DgkKZn2g9yq2HmITJWv6JLknnlVyS7IVCkNjh49s7vZ1kWvrblSZcnJLzTzr9SVw9uU20q9NLr9Aagq/rdAmb5dvMu0nO3RPEZ6taj/daH0DOIJjmyVdl5SA720SYVF1/k61dE9ii6AtZPpmE+l6juL6iuSYsOld8uGprR26pqqZ6so//MdXZq6Z16Vc42qWmaqlC7XcW7f5mY/fuin1VJUThXAO7O2yPYD2ZIYEya3ju5U69cFgNIIqlCmrxbtNNeXDG7ttjGMcrQhV40iQ6R9vL3FrTc7s4+9BHDyqmTTmhq1K/3T+X4arKJmxnZPrHYJ4I4DlP/5Wqaqvteq2uuiTJXlvlO7mDURNVP1zZJdZe6zb87cZLYfHNfNPBYAXI2jEZSZBdAGFcXnXbjD8A5NJCQowDmfyhc6jQ1p11iaNAiTtOx8mb3p6OLGqB7mU7mG9fs9d/N+ZzfFyhZc1vkrqmVc7bMMcK+ujkzVhn2Hq92W3BVzqqq7RlV5tIHRrSd1NNvPTl7n/P/B6mL7yM+rTSn58A6N5fRerDUFoG4QVOEYGxwLIybFhEtcVKhbJ1JrEKK0U5Mv0DkA1h/1n5fvdfdwvFbGEeZTuYJmfzskNJD8QpvMWHd0se3KSv/0xEBNW2HDc2hbfF3qQbPm26rZWr+mNMhxRfe/0i4b1kbax0fJgaw86fPYFGn/wCTnZfq6FHOC7tEzK29OAQA1RVCFY6zdm1mi3t6dHjurhzkDOX5IG/EVZ/Ru6lx49Yhjvhiqh0xVXZQAJlejSQVZKl+gi9laDRus//frmmbpdUF5a16fq2gZ8BNn9zQLx+v8Km1moxdritVNozqaEwgAUFc41YhjWPX1Vr29O7VtEiW3n+xbk4r7tWokzRtGmEUotcWvroWCmgVVLPzrmhLAN2ZsNgtta4e08JCgch9LkwrfXAR46Y4001b9jN51/3pWlqpxVGiF+1pNDG3fWJY+dLJklzpZpR383Fl1AcA/kKnCMdY5zlha9fZwLS0/Od2RrfppGV0Aa4JMlev0bB5rli/QA9HZG+1rwlUWVNGkwnfUd7MK53yqhnWzkHt0eIgkxoSXuBBQAagPBFU4pt7daq/rCZkqX2UtBDx9fUqJ9uCoGoIq1wb5YxwNK6asqbgEkIV/fTNTVZ/lf0c7/1FCCsC3EFShhF2Hjsjh3AIzqbddfJS7h+OzujWNMZ+vThCfUo121ihd/kcFsyuMccyrmrY2pcIucJT/+R7r5JmWI1elA6TL1qhy4XwqAPAEBFUowcpSdUiIZiX5Os4OWNmqn1dQAlhdGWSqXGpQmzizFtzBrDxZtP1QmY/RSf+7D9mzDARVviM2MsQZ4Oi8qrq2N82RqXLBwr8A4Ek4akYJ6/ba6+q7OkpCUHfOcARVOo9FD2ZRddYZdYIq1wgOCpSTulbcBVDLtgqKbBIaFGjmqcB3dGkaU+L///rIVLmynToAeAKCKpTgnE9Fk4p6WSOoe7MYc6A6aSVrVlUHc6rqbiFgLUfVuZXllf61aBRh1luDD86rqo9MlWNOVTMyVQB8DEEVSljrQe3U/YGzBHA5JYDVQVDlesd3bGIWgtW5Nav3ZJTbpKIFpX8+py4yVUt2HJInflkjadlHs/BFRTZJJlMFwEcRVMFJF6Ldtj/LbJOpqh+nO4KqBdsOOg82UDmCKtfTNYNO6BRfbgng0SYVZBh8jVXurXOqNPCpLc103vvNCvnf7K1y+5fLnM+5PytX8gttEhAglJAC8DkEVXDamJJpVp/XRRnjG4S5ezh+QRcBHtC6kWi11S80rKgSPUCjUUXdlgCWHVTRpMJX6SLrOlcuK6/QdICtrZW702VjymGzPWN9qrz/99YSa1QlRIfRCAmAz+F/NRyz6K9mqbQ7Heq3YQUlgFVzOK/ABP8qhqDKpUZ1SZDgwADZsO+wbHVkrUuX/xFU+Wajko6JDUqUgNfGN4t3lSjxe/a3dbJ8ZxprVAHwaQRVcGI+lXuc1rOp6Lz/5bvSZfuBkgeyOFZ6tj1LFRocaErW4Dqa+RvavnGZ2SoW/vVt1v/71sm1msotKJQfl9lPED17Xi85tUeSKfm76fMlsj7Znr1q1pDSPwC+h6AKx2aqaKder+Kjw2RY+yZmm2xV5WinXv8lgLog+AFH23+CKt/U1TGP9u/N+yU7r6DGz/PH2hQz5zEpJlyGd2giz5zXy3SM3HnwiLwxY5N5DJkqAL6IoArOicXrHJmqro5OUHBHF0DPb61eUFhk9pWvFu2UH5bulpz8wnp9fZpU1K0x3ezrVS3dkSb7MnJKZKkaRoZITDifuy8a3LaxaSCxYOtBGfXCTPP7rQs+V9e3jtK/c/s1N6339ff0tYv6mrLSvMIicx+d/wD4IoIqGCmZuXIoO9+UoXVIsNfWo36zAyFBAbJ+X6Zsckzw9iQb9mXKoz+vlv97a470fGSKnPLyX3LPNyvkti+XycjnZ8rHc7eZsp/6QJOKupUQEy59WzU021PW7CvV+Y8sla/q2SJW3rqkn7SMi5B9Gbnm9/v012abxcmrKiUzR2ZuSDXb5/Vv4by9b6tGcvfYzs6vWaMKgC8iqIKx1rE+Sbv4BsxTcYPYyBBzplj96Tgo8STaFnni39tk0fZDciS/UKJCg2RQ2zhzxjk5I0f+/ePqeguuyFTV50LA9hJA5lP5h1N6NJVpd5wg/zqtq0SHB5u/C5e+N1+umLjAnFipzI9L95jsVr9WDc3i5sVdfXw7k5Fv0iBUBrRpVIfvAgDcI9hNrwsPsy6Z+VTuNqJTE5m9ab/M2pAqVx7XVjyFzqdZ4wi6nzm3pwxoEyftmkRJYGCACaC+WrhT3pixWfam24Mr7fz17fXDTEexukBQVT9B1TOT18nczQdMYxA6//mPsOAguXpEO/m//i3klT82yifztpu26Pr/0j8GtZLbR3cy80DLKiG3uv4Vz1JZ9P+LVy/qa5ZE0G0A8DVkqmCscxw0M5/KfU7olGCu5205UO48pazcArnov/PkkZ9W19u4Vu1ON+toNYsNNwdVWh5qHRTpAdj4oW1k1j0j5fGzuktkaJDpYrhid3qdjccKqmLCOSdUl+sWdUpsIAVFNpm+fh/lf36oUVSoPHJmd5l6xwkytnuiWcbgs/k7ZOTzM+T16RvNYvHFrdqdYcqXtSvn6b3sc0TLQkAFwFcRVMEgU+V+ehCrHbNyC4pk/taDZT5m8qpkmbvlgHwwZ5vsOmQ/0K1rur6M6t3SPs+mLFZwdUKnePP1nE1Vn4dRXWSq6rkL4KqjQVXLRgRV/hhgvzN+gHx17VDp3SLWLBD8wpQNcuKLM+W7JbtM5kl9u2SXc7/hdxOAPyKoguQVFDmbI3QhU+U2uuCyFZSUN6/qx2W7ndu/rqifToHLd1UeVFmGOdY4+nvTgTobT8YRe7tnFv6tn6BKy752HrIv2kqmyn/pHMrvbxgur/yjjzRvGGHKfe/4armc+cZs8/+V9X/Tef2au3uoAOAWBFWQzamHTZmPTkzWEi+4zwmd450HsmV11vq7WAbop3pa02r5TnspX+8WVQiqOtjX21q841CdtVonU1U/ujeLMQfP2phET7xoe+ymLNrq17R076w+zeWPO0+Q+07tItFhwabsb8L7C0z32MSYMDm+o/3/MADwNwRVOLo+VVKMyZbAfXSxTD141cxh6fI+zUxppY3OadI1X1bvyTABcV3SQG532hGzfo22XK6MNrDQEkY9CF+07VCdjImgqn7o/wVjutvXrFLNGoZLSB01H4F30Q6x153QXmbePVIuG9ra/J+lzuvXwrkNAP6Gv5CQdXsd86maMp/K3TRQ6Osos/tzQ8l5ST8us2emLhncSo7raM8I/VzH2aoVjixVx4QG0iAsuEoH4sM6OEoAN9fNvCrWqar/EkBF6R9Ka9wgTB49q4dMuX2EPH1uT7nlpI7uHhIAuA1BlZ/TEq05m+3zX7okMZ/KE4xwzKuatSHFedv2A1mybGeaWZx5XK+mZr0XK6jSVsZ1Pp+qCqV/luHtm9RpswpnpiqSoKquDWwTJ3FRoWabJhUoj65JddGgVqxxCMCvEVT5sZSMHLnwv/Nk5e50CQkKcDYZgHsd7aB3QPILi8z2T44slZYHJkSHy8ndEk3r4s2pWbLWkWmsCxrIVbVJhUXHqHS/sgIgV9EA8mhLdYKquqalXON6NjXb3ZtXXv4JAIC/IqjyU7r20Flv/G3aZTeMDJGPrhwsbZpEuXtYEJGezWNNdiAzt0CW7kgzgcQPjs5aVoYqOjxETuycUKcNK7RVstVOvU81gqqk2HBpFx9l5n/pmluulJ1XaJqqKMr/6se/xnWVdycMkH8MbOnuoQAA4LEIqvzQb6uS5fy355qWuO3jo+SHG4bLULJUHtVh63jHnCktAVyzVxtSZJnM1NgeR+e4nNmnbksAtx3IkoycAvO6nau5flldlQBm5NizVNqoQxcaRt3Tki7NjNKkAgCA8vFX0s/oWiLXfbLYtEnWA/fvbhhOhsqDSwC1tbrVoGJ014QSJW+jOidIVGiQ6c63ZIc9o1QX86l6NIup9gH1cGezigN11vmPTpUAAMBTEFT5mU/n7TDXFwxoIRMvH0gJlYey1nrRNWC+XbzLbJ/Zu+SimhGh9gxCXXUBdK5PVY3SP8uQdo1NG3ZtDb8vI8dlY0rPpvMfAADwPARVfmbrgSxzfemQ1hJMOY/Hio8Okx7N7d0YD2TlmYWZRzoWBi7OKgH8deVeKXTMNXJ1k4rqzKeyNIwMlR7N7I0N5riwtbqzSQVBFQAA8CCVLzwDn3E4t0BSM3PNduvGlPx5uhEd402mSp3aI6nMdsXHdYg3WRv9uc7fckCGOTrv6RyrnPwiyczNl8M5BeZnn5ljv+j24Zx857aGYlcf384EchZdvHfNnowaB1VK16vSDoB/bzog5/RtIa7Awr8AAMATEVT5kW377Vkq7SzHQal3zKt6c+Zms31Wn5KlfxZtIqEB1xcLd8otXyw1gZc9aCpwdsmrCg2gPr5qkHOe0rrkDMkrLDKdIWu66Ks2q3hn1haZu/mACfJcMQeKTBUAAPBEBFV+RLu5qTaNWcTTG/Rr3Uj6t25k1grSOUrl+b/+LUxQtf9w3jH3aRzTICxYosOCpUF4sH07PMRs622RocHy2YLtMnvTfvlswQ65ZHBr831WK3Vd9LemwZAuHBsaFGgaaWw/kO2ShigZzkwV/3UBAADPwZGJH9EDW0W3P++gHfe+vX5YpY8b0CZOfrxxuMniaLAUY4Ine+AUGRJkWrRXpEWjCHnslzXy5K9rTclhy7hIWVaLJhXFG2n0bdVQ5m89KH9v3u+S/e5gtj1wbBQZWuvnAgAAcBW3dip4+umnZeDAgRIdHS0JCQly9tlny/r16533Hzx4UG6++Wbp3LmzRERESKtWreSWW26R9HT7AZ9lx44dMm7cOImMjDTPc/fdd0tBQYEb3pFn2+oo/2vLfCqfo8HPiE7x0q9VI+mQEG0W4NWsVGUBlbp8WBsZ1DbOLKx79zfL7Yv+Otqp92lpbzZRU8Mdc7zmbDrg0hMDGggCAAB4CrcGVbNmzZIbb7xR5s2bJ1OnTpX8/HwZM2aMZGXZD/737NljLi+88IKsWrVKPvjgA/ntt9/kqquucj5HYWGhCajy8vJkzpw58uGHH5rHPfTQQ258Z549p4pMFYrTwOuF/+ttFtOdt+WgvDlzk2xOPWzu69Wi5pmq4utVaQdADdZqa8dBe1BFoxUAAOBJAmw6g9xDpKammkyTBlsjRowo8zFff/21XHrppSbwCg4OlsmTJ8vpp59ugq/ERPuaPW+//bbce++95vlCQysvE8rIyJDY2FiTAYuJsbex9kUDnphq5t38cvNx0qN57TIQ8D0fz90m//5xtfNrzQbNvvfEWj1nfmGR9Hl0imTlFcqvtxwn3R1t1mv6XF3//ZtpwDH3/hOlaSzZKgAA4Ho1iQ08aqEiq6wvLi6uwsfom9OASs2dO1d69uzpDKjU2LFjzYexevXRA8TicnNzzf3FL74uMyff2cigNY0qUAZtUjGs/dGGGLWZT1V8XpiWFrqiBHBP2hETUIUFB0pidHitxwYAAOAqHhNUFRUVyW233SbDhw+XHj16lPmY/fv3y+OPPy7XXHON87bk5OQSAZWyvtb7ypvLpdGndWnZsqX4um377WVTTRqEmu5vQFllgM+e10uiQu3rYfWpZelf6XlV2qzCFfOptMV7VeaKAQAA+F1QpXOrdN7UF198Ueb9mk3SuVPdunWTRx55pFavdf/995uMl3XZuXOn+LqtznbqzEVB+bTz3+uX9JNxvZqaVu2uMKy9PahasPWgWVS4prY751ORaQUAAJ7FI1qq33TTTfLLL7/In3/+KS1aHHsgl5mZKaeccorpEvj9999LSMjRTEtSUpIsWLCgxOP37dvnvK8sYWFh5uJPttOkAlU0qnOCubhKl6Ros+D0waw801VQ16+qzT5MkwoAAOBp3Jqp0h4ZGlBpoDR9+nRp27ZtmRkq7QioDSd++uknCQ8vOZdi6NChsnLlSklJSXHepp0Edd6VZrVQMlPVlqAK9UxL9YY65mr9vanmJYBkqgAAgKcKdHfJ3yeffCKfffaZyULpHCi9HDlypERApZ3+3nvvPfO19Rhtpa70fg2exo8fL8uXL5fff/9dHnzwQfPc/paNqlI7dc7yww2GO0oAa9OsYkexOVUAAACexK3lf2+99Za5HjlyZInbJ06cKJdffrksWbJE5s+fb27r0KFDicds3bpV2rRpI0FBQaZ08PrrrzdZq6ioKLnsssvkscceq8d34vm2OQ5I2zThgBT1z1qvaunOQ5KdVyCRocHVzmpvP8iJAQAA4JncGlRVtkSWBltVWUardevWMmnSJBeOzLekH8k381kUB6RwB80uNW8YIbvTjpiGFSOrOWcrJTNXcvKLJCgwQJo3Yn0qAADgWTym+x/qvvQvITpMosI8ojcJ/ExAQIAzWzVn84Eat1PXwEzXvgIAAPAkHJ34gW20U4cHcK5XVYNmFdY+TJMKAADgiQiq/IC18C/zqeBOVgfANXsz5JCjHLWqaFIBAAA8GUGVP2WqaKcON0qIDpdOiQ1Ep0nO3XKgRu3UybYCAABPRFDlB7Y65lS15YAUbjasfc1KALc7Tgy0ovwPAAB4IIIqP0CmCp42r6q6zSqsRhXMqQIAAJ6IoMrHpWXnSVp2vtmmdAruNrhdnAQG2LOne9Lsi3xXZR/WZQEUc6oAAIAnIqjyk9K/pJhwiQgNcvdw4OdiwkOkV4uG1cpWWVkqXRKguosGAwAA1AeCKr8p/eMMPzzDMEcXwDlVnFdlNamg9A8AAHgqgip/aadO6R88bb2qzfvFpq0AK7HDuUYV+zAAAPBMBFU+jiYV8DT9WzeS0OBA2ZeRK5tT7ftnRbZZTSqYTwUAADwUQZWP2+aYU0WmCp4iPCRIBrRuZLbnbN5f5YV/W3NiAAAAeCiCKh+mpVXONao4IIUnlgBWYV7V9oOO8j8yVQAAwEMRVPmwQ9n5kpFTYLaZ5A9PbFYxd/MBKSwqf17VkbxCUyao2IcBAICnIqjyYVaWqllsuCm5AjxFz+axEh0WbIL+1XvSy33cDkfnv9iIEGkYGVqPIwQAAKg6gip/mE9F6R88THBQoAxuZ89W/b2p/PWqtjs7/5GlAgAAnougyoet3G3PABBUwRMN79C40mYV1sK/rZhPBQAAPBhBlY96f/ZW+WDONrM9sI290xrgic0qFm47KLkFhRU2qaB7JQAA8GQEVT7ojRmb5LFf1pjta0a0k7P7NHf3kIBjdExoIPHRYZKTXyRLtqdVnKmi/A8AAHgwgiofa6H+3G/r5Pnf15uvbx/dSe4/tYsEBAS4e2jAMXS/tLoAllcCaAVVtFMHAACejKDKRxQV2eTRn9fImzM3m6//dVpXuXV0RwIqeLTh7ctfryq/sEh2px0x28wLBAAAnizY3QNA7ek6P/d/t0K+WrRLNIZ64uwecsng1u4eFlCpYY5mFct3pUtmTr5Eh4c479t96IjZt8NDAiUhOsyNowQAAKgYmSovp2fzb/1iqQmoAgNEXjy/NwEVvEaLRpGmXboGTwu2Hixx33bHGlWt46LIuAIAAI9GUOXFcvIL5fpPFssvK/ZKSFCAvHlJPzm3Xwt3DwuolmHOEsCj61VpkPXz8j1mmyYVAADA0xFUeansvAL554eLZNraFAkLDpT/Thggp/Ro6u5hAbVer+pIXqHc8Oli+WbxLvM13SsBAICnY06VF8rIyZcrJy6URdsPSVRokPzvsoEy1NFFDfA2Q9vZ9911yZmyYV+m3PPNClm2M01CgwLlxQt6y7henCwAAACejaDKyxzMypPL3l8gK3enS0x4sHx45SDp24rFfeG9GjcIky5J0SaoOuv1v+VIfqHERoTIuxMGyKC2ce4eHgAAQKUo//MiKZk58o//zjUBVeOoUPnimqEEVPAJwzvY51VpQNUyLkK+u2EYARUAAPAaBFVeQtfrueDtubJh32FJjAmTL68dKt2axbh7WIBLnNbTXuLXp2VD+f6G4dI+voG7hwQAAFBllP95ga37s+TS/803gVWLRhHy2T+H0BENPqV/60ay8F+jTQY2UNcGAAAA8CIEVR4uLTtPLnxnrqRk5kq7+Cj59J+DpWlshLuHBbhcPAv8AgAAL0VQ5eFmrk81AZXOM/nymqEceAIAAAAehjlVHm7t3gxzPapzAgEVAAAA4IEIqjzcGkdQ1bUpTSkAAAAAT0RQ5eHW7s001wRVAAAAgGciqPJgqZm5sv9wrmgztM6J0e4eDgAAAIAyEFR5wXyqNk2iJCI0yN3DAQAAAFAGgiovCKoo/QMAAAA8F0GVFzSp6EZQBQAAAHgsgiqvyFQxnwoAAADwVARVHionv1A2p2aZ7W5NY909HAAAAADlIKjyUJtSDkthkU0aRYZIYgyL/gIAAACeiqDKCxb9DQgIcPdwAAAAAJSDoMpD0fkPAAAA8A4EVR6KoAoAAADwDgRVHshms8maPXT+AwAAALwBQZUH2pOeIxk5BRIcGCAdEhq4ezgAAAAAKkBQ5YHWOrJUGlCFBQe5ezgAAAAAKkBQ5YGYTwUAAAB4D4IqD7Q22R5UdSOoAgAAADweQZUHWrs301yTqQIAAAA8H0GVh8nOK5BtB7LMNp3/AAAAAM9HUOVh1iVnis0mkhAdJo0bhLl7OAAAAAAqQVDlYY6uT0XpHwAAAOANCKo8DJ3/AAAAAO9CUOWxQRXzqQAAAABvQFDlQYqKbGZOlaKdOgAAAOAdCKo8yI6D2ZKdVyhhwYHStkmUu4cDAAAAoAqCq/Ig1I+8wiIZ2TleggICJDiIeBcAAADwBgRVHqRTYrR8cMUgdw8DAAAAQDWQDgEAAACAWiCoAgAAAIBaIKgCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAgFoIrs03+wqbzWauMzIy3D0UAAAAAG5kxQRWjFAVBFUikpmZaa5btmzp7qEAAAAA8JAYITY2tkqPDbBVJwTzUUVFRbJ+/Xrp1q2b7Ny5U2JiYtw9JPjY2Q4N2Nm3UFvsS6hL7F9wFfYlePu+peGRBlTNmjWTwMCqzZYiU6UTywIDpXnz5mZbf0D8B4C6wL4FV2FfQl1i/4KrsC/Bm/etqmaoLDSqAAAAAIBaIKgCAAAAgFogqHIICwuThx9+2FwDrsS+BVdhX0JdYv+Cq7AvwR/3LRpVAAAAAEAtkKkCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAAF8Nqp5++mkZOHCgREdHS0JCgpx99tmyfv36Eo/JycmRG2+8URo3biwNGjSQ8847T/bt2+e8f/ny5XLRRReZ1ZcjIiKka9eu8sorr5T7mn///bcEBwdLnz59Kh2f9vh46KGHpGnTpua5R48eLRs3bizxmA0bNshZZ50lTZo0MYuUHXfccTJjxowafR5wLV/Yv5YsWSInn3yyNGzY0IzxmmuukcOHD9fo84Bv7kffffedjBkzxrx2QECALFu27JjHVDY+uI8v7F///e9/ZeTIkeZvoD4mLS2t2p8Das/b96WDBw/KzTffLJ07dzav3apVK7nlllskPT29Rp8HvG/fmjlzptk3Sl+Sk5NrfTz15JNPyrBhwyQyMtIcU/lcUDVr1izzA5g3b55MnTpV8vPzzS9cVlaW8zG33367/Pzzz/L111+bx+/Zs0fOPfdc5/2LFy82P+BPPvlEVq9eLf/617/k/vvvl9dff/2Y19P/6CdMmCAnnXRSlcb33HPPyauvvipvv/22zJ8/X6KiomTs2LFmx7GcfvrpUlBQINOnTzdj6d27t7mtsh0Adc/b9y8di/7H0KFDB3P/b7/9ZsZw+eWXu+TzgW/sRzoOPZnz7LPPlvuYysYH9/GF/Ss7O1tOOeUUeeCBB6r9/uE63r4v6Vj08sILL8iqVavkgw8+MH/3rrrqqhp9HvDefWv9+vWyd+9e50W/r7bH63l5eXL++efL9ddfX/MPwuZFUlJStP27bdasWebrtLQ0W0hIiO3rr792Pmbt2rXmMXPnzi33eW644QbbqFGjjrn9wgsvtD344IO2hx9+2Na7d+8Kx1JUVGRLSkqyPf/8887bdDxhYWG2zz//3HydmppqxvLnn386H5ORkWFumzp1ajXfPeqat+1f77zzji0hIcFWWFjofMyKFSvM+DZu3FjNdw9f3I+K27p1q3nNpUuXlri9puODe3jb/lXcjBkzzGMOHTpU5edF3fHmfcny1Vdf2UJDQ235+flVfn547741owb/h1TleKq4iRMn2mJjY2014dGZqtKsFG9cXJwzqtVoWM/WW7p06WJSwnPnzq3weaznsEycOFG2bNliFhSriq1bt5psU/HXjo2NlcGDBztfW1Ocmqb+6KOPTLSuGat33nnHRNT9+/ev5rtHXfO2/Ss3N1dCQ0MlMPDor7GmtdXs2bOr+K7hy/tRVdR0fHAPb9u/4Ll8YV/S19ayUi0xhH/sW0rLSbWUT6c/aIlpbY+nXMVr9sKioiK57bbbZPjw4dKjRw9zm35IelBZuvYxMTGx3PK6OXPmyJdffim//vqr8zatq7zvvvvkr7/+qvIvpvX8+lrlvbbWeU6bNs3UlmqdqR78akCl6epGjRpV8xNAXfLG/evEE0+UO+64Q55//nm59dZbTeCur6M0HY7652n7UVXUZHxwD2/cv+CZfGFf2r9/vzz++ONmLjH8Y99q2rSpKeEbMGCAObH8v//9z8zX1JK+fv361fh4ylW8JlOltZpaQ/vFF1/U+Dn0+7VphJ450VpPVVhYKBdffLE8+uij0qlTpzK/79NPPzWT6qyL/kdRFToxTsetgZR+z4IFC0yAdcYZZ3DQ62G8cf/q3r27fPjhh/Liiy+aiZVJSUnStm1b8x9F8ewV6o837kfwHuxfcBVv35cyMjJk3Lhx0q1bN3nkkUdq/B7gPfuW0uqva6+91lR7aVOJ999/31y/9NJLnvH/lM0L3HjjjbYWLVrYtmzZUuL2P/74o8zaylatWtn+85//lLht9erVZv7JAw88UOJ2/V59jqCgIOclICDAeZu+hs6D0jkq1iU7O9u2efPmMmt+R4wYYbvlllvM9rRp02yBgYG29PT0Eo/p0KGD7emnn3bJZwP/3b+KS05OtmVmZtoOHz5s9jmtM0f98sT9qCrzFKozPriPt+5fxTGnyjN4+76k3z906FDbSSedZDty5EgtPw14y75Vnrvuuss2ZMgQs+2K46nazKny6KBKJ5fpD6hZs2a2DRs2HHO/NfHtm2++cd62bt26Yya+rVq1yvyA7r777mOeQyf5r1y5ssTl+uuvt3Xu3Nls60FqRRPfXnjhBedtGjwVn/j2008/mQNcPdgtrlOnTrYnn3yyhp8KXMXb96+yvPfee7bIyEgOWuqRJ+9H1WlUUdn44B7evn8VR1DlXr6wL+nfQT2APuGEE2xZWVnV/ATgzftWeUaPHm0755xzyr2/usdTPhtU6S+ivrGZM2fa9u7d67wUP6tx3XXXmUh3+vTptkWLFpmzF3qx6C9xfHy87dJLLy3xHNqZpDxV7VTzzDPP2Bo2bGj78ccfTde1s846y9a2bVvnmRPt/te4cWPbueeea1u2bJlt/fr1JqLWHUu/hnt5+/6lXnvtNdvixYvNvvX666/bIiIibK+88kqtPhf41n504MABc3Dy66+/mj9gX3zxhflan7+q44P7+ML+pdt627vvvuvsiKtf6/ei/nj7vqQHwoMHD7b17NnTtmnTphKvX1BQUOvPB56/b7300ku2H374wWSh9PG33nqrSV5oZVhtj6e2b99u9rdHH33U1qBBA7Otl9KJEa8NqvSXqqyLRpEW/UC05WKjRo3MGXqNVov/Z66/zGU9R+vWrWv9H4BGv//+979tiYmJJuLVVLQe3Ba3cOFC25gxY2xxcXG26Ohoc4Zl0qRJNf5M4Dq+sH+NHz/e7FvaUrZXr162jz76qMafB3xzP9JxlPXc+v1VHR/cxxf2r/Jev/h7QN3z9n3JynSWddHsFnx/33r22Wdt7du3t4WHh5tjn5EjR5ogzRXHU5dddlmZr6/7XVUFOD4MAAAAAEAN0CIMAAAAAGqBoAoAAAAAaoGgCgAAAABqgaAKAAAAAGqBoAoAAAAAaoGgCgAAAABqgaAKAAAAAGqBoAoAAAAAaoGgCgAAAABqgaAKAOBTLr/8cgkICDCXkJAQSUxMlJNPPlnef/99KSoqqvLzfPDBB9KwYcM6HSsAwDcQVAEAfM4pp5wie/fulW3btsnkyZNl1KhRcuutt8rpp58uBQUF7h4eAMDHEFQBAHxOWFiYJCUlSfPmzaVfv37ywAMPyI8//mgCLM1Aqf/85z/Ss2dPiYqKkpYtW8oNN9wghw8fNvfNnDlTrrjiCklPT3dmvR555BFzX25urtx1113mufV7Bw8ebB4PAPBfBFUAAL9w4oknSu/eveW7774zXwcGBsqrr74qq1evlg8//FCmT58u99xzj7lv2LBh8vLLL0tMTIzJeOlFAyl10003ydy5c+WLL76QFStWyPnnn28yYxs3bnTr+wMAuE+AzWazufH1AQBw+ZyqtLQ0+eGHH4657x//+IcJhNasWXPMfd98841cd911sn//fvO1ZrRuu+0281yWHTt2SLt27cx1s2bNnLePHj1aBg0aJE899VSdvS8AgOcKdvcAAACoL3oeUUv51LRp0+Tpp5+WdevWSUZGhplrlZOTI9nZ2RIZGVnm969cuVIKCwulU6dOJW7XksDGjRvXy3sAAHgegioAgN9Yu3attG3b1jSw0KYV119/vTz55JMSFxcns2fPlquuukry8vLKDap0zlVQUJAsXrzYXBfXoEGDenoXAABPQ1AFAPALOmdKM0233367CYq0vfqLL75o5lapr776qsTjQ0NDTVaquL59+5rbUlJS5Pjjj6/X8QMAPBdBFQDA52g5XnJysgmA9u3bJ7/99psp9dPs1IQJE2TVqlWSn58vr732mpxxxhny999/y9tvv13iOdq0aWMyU3/88YdpcKHZKy37u+SSS8xzaECmQVZqaqp5TK9evWTcuHFue88AAPeh+x8AwOdoENW0aVMTGGlnvhkzZphOf9pWXcv2NEjSlurPPvus9OjRQz799FMTdBWnHQC1ccWFF14o8fHx8txzz5nbJ06caIKqO++8Uzp37ixnn322LFy4UFq1auWmdwsAcDe6/wEAAABALZCpAgAAAIBaIKgCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAgFogqAIAAACAWiCoAgAAAIBaIKgCAAAAAKm5/weKfJwdC1mgUAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10, 6))\n",
    "plt.plot(data.index[-100:], data['Close'][-100:], label=\"Actual Data\")\n",
    "plt.plot(test.index, forecast, label=\"Forecast\", color='orange')\n",
    "plt.title(\"Stock Price Prediction with ARIMA\")\n",
    "plt.xlabel(\"Date\")\n",
    "plt.ylabel(\"Price\")\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/20\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/titiksha/dev/cla_christmas_break/.venv/lib/python3.10/site-packages/keras/src/layers/rnn/rnn.py:200: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.\n",
      "  super().__init__(**kwargs)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 15ms/step - loss: 0.2666\n",
      "Epoch 2/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 15ms/step - loss: 0.0147\n",
      "Epoch 3/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0135\n",
      "Epoch 4/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0126\n",
      "Epoch 5/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0119\n",
      "Epoch 6/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 17ms/step - loss: 0.0097\n",
      "Epoch 7/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0108\n",
      "Epoch 8/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0099\n",
      "Epoch 9/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0102\n",
      "Epoch 10/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0109\n",
      "Epoch 11/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0108\n",
      "Epoch 12/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0113\n",
      "Epoch 13/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0090\n",
      "Epoch 14/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0106\n",
      "Epoch 15/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0086\n",
      "Epoch 16/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0085\n",
      "Epoch 17/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0095\n",
      "Epoch 18/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0093\n",
      "Epoch 19/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 16ms/step - loss: 0.0089\n",
      "Epoch 20/20\n",
      "\u001b[1m77/77\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 19ms/step - loss: 0.0091\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.src.callbacks.history.History at 0x17578c7f0>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow.keras.models import Sequential\n",
    "from tensorflow.keras.layers import LSTM, Dense, Dropout\n",
    "import numpy as np\n",
    "\n",
    "# Preprocess data\n",
    "prices = data['Close'].values.reshape(-1, 1)\n",
    "scaled_prices = (prices - prices.mean()) / prices.std()\n",
    "\n",
    "# Prepare training data\n",
    "window_size = 60\n",
    "X, y = [], []\n",
    "for i in range(window_size, len(scaled_prices)):\n",
    "    X.append(scaled_prices[i-window_size:i, 0])\n",
    "    y.append(scaled_prices[i, 0])\n",
    "X, y = np.array(X), np.array(y)\n",
    "\n",
    "# Build LSTM model\n",
    "model = Sequential([\n",
    "    LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)),\n",
    "    Dropout(0.2),\n",
    "    LSTM(units=50),\n",
    "    Dropout(0.2),\n",
    "    Dense(units=1)\n",
    "])\n",
    "\n",
    "model.compile(optimizer='adam', loss='mean_squared_error')\n",
    "model.fit(X, y, epochs=20, batch_size=32)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "mode": "lines",
         "name": "Actual",
         "type": "scatter",
         "x": [
          "2015-01-02T00:00:00",
          "2015-01-05T00:00:00",
          "2015-01-06T00:00:00",
          "2015-01-07T00:00:00",
          "2015-01-08T00:00:00",
          "2015-01-09T00:00:00",
          "2015-01-12T00:00:00",
          "2015-01-13T00:00:00",
          "2015-01-14T00:00:00",
          "2015-01-15T00:00:00",
          "2015-01-16T00:00:00",
          "2015-01-20T00:00:00",
          "2015-01-21T00:00:00",
          "2015-01-22T00:00:00",
          "2015-01-23T00:00:00",
          "2015-01-26T00:00:00",
          "2015-01-27T00:00:00",
          "2015-01-28T00:00:00",
          "2015-01-29T00:00:00",
          "2015-01-30T00:00:00",
          "2015-02-02T00:00:00",
          "2015-02-03T00:00:00",
          "2015-02-04T00:00:00",
          "2015-02-05T00:00:00",
          "2015-02-06T00:00:00",
          "2015-02-09T00:00:00",
          "2015-02-10T00:00:00",
          "2015-02-11T00:00:00",
          "2015-02-12T00:00:00",
          "2015-02-13T00:00:00",
          "2015-02-17T00:00:00",
          "2015-02-18T00:00:00",
          "2015-02-19T00:00:00",
          "2015-02-20T00:00:00",
          "2015-02-23T00:00:00",
          "2015-02-24T00:00:00",
          "2015-02-25T00:00:00",
          "2015-02-26T00:00:00",
          "2015-02-27T00:00:00",
          "2015-03-02T00:00:00",
          "2015-03-03T00:00:00",
          "2015-03-04T00:00:00",
          "2015-03-05T00:00:00",
          "2015-03-06T00:00:00",
          "2015-03-09T00:00:00",
          "2015-03-10T00:00:00",
          "2015-03-11T00:00:00",
          "2015-03-12T00:00:00",
          "2015-03-13T00:00:00",
          "2015-03-16T00:00:00",
          "2015-03-17T00:00:00",
          "2015-03-18T00:00:00",
          "2015-03-19T00:00:00",
          "2015-03-20T00:00:00",
          "2015-03-23T00:00:00",
          "2015-03-24T00:00:00",
          "2015-03-25T00:00:00",
          "2015-03-26T00:00:00",
          "2015-03-27T00:00:00",
          "2015-03-30T00:00:00",
          "2015-03-31T00:00:00",
          "2015-04-01T00:00:00",
          "2015-04-02T00:00:00",
          "2015-04-06T00:00:00",
          "2015-04-07T00:00:00",
          "2015-04-08T00:00:00",
          "2015-04-09T00:00:00",
          "2015-04-10T00:00:00",
          "2015-04-13T00:00:00",
          "2015-04-14T00:00:00",
          "2015-04-15T00:00:00",
          "2015-04-16T00:00:00",
          "2015-04-17T00:00:00",
          "2015-04-20T00:00:00",
          "2015-04-21T00:00:00",
          "2015-04-22T00:00:00",
          "2015-04-23T00:00:00",
          "2015-04-24T00:00:00",
          "2015-04-27T00:00:00",
          "2015-04-28T00:00:00",
          "2015-04-29T00:00:00",
          "2015-04-30T00:00:00",
          "2015-05-01T00:00:00",
          "2015-05-04T00:00:00",
          "2015-05-05T00:00:00",
          "2015-05-06T00:00:00",
          "2015-05-07T00:00:00",
          "2015-05-08T00:00:00",
          "2015-05-11T00:00:00",
          "2015-05-12T00:00:00",
          "2015-05-13T00:00:00",
          "2015-05-14T00:00:00",
          "2015-05-15T00:00:00",
          "2015-05-18T00:00:00",
          "2015-05-19T00:00:00",
          "2015-05-20T00:00:00",
          "2015-05-21T00:00:00",
          "2015-05-22T00:00:00",
          "2015-05-26T00:00:00",
          "2015-05-27T00:00:00",
          "2015-05-28T00:00:00",
          "2015-05-29T00:00:00",
          "2015-06-01T00:00:00",
          "2015-06-02T00:00:00",
          "2015-06-03T00:00:00",
          "2015-06-04T00:00:00",
          "2015-06-05T00:00:00",
          "2015-06-08T00:00:00",
          "2015-06-09T00:00:00",
          "2015-06-10T00:00:00",
          "2015-06-11T00:00:00",
          "2015-06-12T00:00:00",
          "2015-06-15T00:00:00",
          "2015-06-16T00:00:00",
          "2015-06-17T00:00:00",
          "2015-06-18T00:00:00",
          "2015-06-19T00:00:00",
          "2015-06-22T00:00:00",
          "2015-06-23T00:00:00",
          "2015-06-24T00:00:00",
          "2015-06-25T00:00:00",
          "2015-06-26T00:00:00",
          "2015-06-29T00:00:00",
          "2015-06-30T00:00:00",
          "2015-07-01T00:00:00",
          "2015-07-02T00:00:00",
          "2015-07-06T00:00:00",
          "2015-07-07T00:00:00",
          "2015-07-08T00:00:00",
          "2015-07-09T00:00:00",
          "2015-07-10T00:00:00",
          "2015-07-13T00:00:00",
          "2015-07-14T00:00:00",
          "2015-07-15T00:00:00",
          "2015-07-16T00:00:00",
          "2015-07-17T00:00:00",
          "2015-07-20T00:00:00",
          "2015-07-21T00:00:00",
          "2015-07-22T00:00:00",
          "2015-07-23T00:00:00",
          "2015-07-24T00:00:00",
          "2015-07-27T00:00:00",
          "2015-07-28T00:00:00",
          "2015-07-29T00:00:00",
          "2015-07-30T00:00:00",
          "2015-07-31T00:00:00",
          "2015-08-03T00:00:00",
          "2015-08-04T00:00:00",
          "2015-08-05T00:00:00",
          "2015-08-06T00:00:00",
          "2015-08-07T00:00:00",
          "2015-08-10T00:00:00",
          "2015-08-11T00:00:00",
          "2015-08-12T00:00:00",
          "2015-08-13T00:00:00",
          "2015-08-14T00:00:00",
          "2015-08-17T00:00:00",
          "2015-08-18T00:00:00",
          "2015-08-19T00:00:00",
          "2015-08-20T00:00:00",
          "2015-08-21T00:00:00",
          "2015-08-24T00:00:00",
          "2015-08-25T00:00:00",
          "2015-08-26T00:00:00",
          "2015-08-27T00:00:00",
          "2015-08-28T00:00:00",
          "2015-08-31T00:00:00",
          "2015-09-01T00:00:00",
          "2015-09-02T00:00:00",
          "2015-09-03T00:00:00",
          "2015-09-04T00:00:00",
          "2015-09-08T00:00:00",
          "2015-09-09T00:00:00",
          "2015-09-10T00:00:00",
          "2015-09-11T00:00:00",
          "2015-09-14T00:00:00",
          "2015-09-15T00:00:00",
          "2015-09-16T00:00:00",
          "2015-09-17T00:00:00",
          "2015-09-18T00:00:00",
          "2015-09-21T00:00:00",
          "2015-09-22T00:00:00",
          "2015-09-23T00:00:00",
          "2015-09-24T00:00:00",
          "2015-09-25T00:00:00",
          "2015-09-28T00:00:00",
          "2015-09-29T00:00:00",
          "2015-09-30T00:00:00",
          "2015-10-01T00:00:00",
          "2015-10-02T00:00:00",
          "2015-10-05T00:00:00",
          "2015-10-06T00:00:00",
          "2015-10-07T00:00:00",
          "2015-10-08T00:00:00",
          "2015-10-09T00:00:00",
          "2015-10-12T00:00:00",
          "2015-10-13T00:00:00",
          "2015-10-14T00:00:00",
          "2015-10-15T00:00:00",
          "2015-10-16T00:00:00",
          "2015-10-19T00:00:00",
          "2015-10-20T00:00:00",
          "2015-10-21T00:00:00",
          "2015-10-22T00:00:00",
          "2015-10-23T00:00:00",
          "2015-10-26T00:00:00",
          "2015-10-27T00:00:00",
          "2015-10-28T00:00:00",
          "2015-10-29T00:00:00",
          "2015-10-30T00:00:00",
          "2015-11-02T00:00:00",
          "2015-11-03T00:00:00",
          "2015-11-04T00:00:00",
          "2015-11-05T00:00:00",
          "2015-11-06T00:00:00",
          "2015-11-09T00:00:00",
          "2015-11-10T00:00:00",
          "2015-11-11T00:00:00",
          "2015-11-12T00:00:00",
          "2015-11-13T00:00:00",
          "2015-11-16T00:00:00",
          "2015-11-17T00:00:00",
          "2015-11-18T00:00:00",
          "2015-11-19T00:00:00",
          "2015-11-20T00:00:00",
          "2015-11-23T00:00:00",
          "2015-11-24T00:00:00",
          "2015-11-25T00:00:00",
          "2015-11-27T00:00:00",
          "2015-11-30T00:00:00",
          "2015-12-01T00:00:00",
          "2015-12-02T00:00:00",
          "2015-12-03T00:00:00",
          "2015-12-04T00:00:00",
          "2015-12-07T00:00:00",
          "2015-12-08T00:00:00",
          "2015-12-09T00:00:00",
          "2015-12-10T00:00:00",
          "2015-12-11T00:00:00",
          "2015-12-14T00:00:00",
          "2015-12-15T00:00:00",
          "2015-12-16T00:00:00",
          "2015-12-17T00:00:00",
          "2015-12-18T00:00:00",
          "2015-12-21T00:00:00",
          "2015-12-22T00:00:00",
          "2015-12-23T00:00:00",
          "2015-12-24T00:00:00",
          "2015-12-28T00:00:00",
          "2015-12-29T00:00:00",
          "2015-12-30T00:00:00",
          "2015-12-31T00:00:00",
          "2016-01-04T00:00:00",
          "2016-01-05T00:00:00",
          "2016-01-06T00:00:00",
          "2016-01-07T00:00:00",
          "2016-01-08T00:00:00",
          "2016-01-11T00:00:00",
          "2016-01-12T00:00:00",
          "2016-01-13T00:00:00",
          "2016-01-14T00:00:00",
          "2016-01-15T00:00:00",
          "2016-01-19T00:00:00",
          "2016-01-20T00:00:00",
          "2016-01-21T00:00:00",
          "2016-01-22T00:00:00",
          "2016-01-25T00:00:00",
          "2016-01-26T00:00:00",
          "2016-01-27T00:00:00",
          "2016-01-28T00:00:00",
          "2016-01-29T00:00:00",
          "2016-02-01T00:00:00",
          "2016-02-02T00:00:00",
          "2016-02-03T00:00:00",
          "2016-02-04T00:00:00",
          "2016-02-05T00:00:00",
          "2016-02-08T00:00:00",
          "2016-02-09T00:00:00",
          "2016-02-10T00:00:00",
          "2016-02-11T00:00:00",
          "2016-02-12T00:00:00",
          "2016-02-16T00:00:00",
          "2016-02-17T00:00:00",
          "2016-02-18T00:00:00",
          "2016-02-19T00:00:00",
          "2016-02-22T00:00:00",
          "2016-02-23T00:00:00",
          "2016-02-24T00:00:00",
          "2016-02-25T00:00:00",
          "2016-02-26T00:00:00",
          "2016-02-29T00:00:00",
          "2016-03-01T00:00:00",
          "2016-03-02T00:00:00",
          "2016-03-03T00:00:00",
          "2016-03-04T00:00:00",
          "2016-03-07T00:00:00",
          "2016-03-08T00:00:00",
          "2016-03-09T00:00:00",
          "2016-03-10T00:00:00",
          "2016-03-11T00:00:00",
          "2016-03-14T00:00:00",
          "2016-03-15T00:00:00",
          "2016-03-16T00:00:00",
          "2016-03-17T00:00:00",
          "2016-03-18T00:00:00",
          "2016-03-21T00:00:00",
          "2016-03-22T00:00:00",
          "2016-03-23T00:00:00",
          "2016-03-24T00:00:00",
          "2016-03-28T00:00:00",
          "2016-03-29T00:00:00",
          "2016-03-30T00:00:00",
          "2016-03-31T00:00:00",
          "2016-04-01T00:00:00",
          "2016-04-04T00:00:00",
          "2016-04-05T00:00:00",
          "2016-04-06T00:00:00",
          "2016-04-07T00:00:00",
          "2016-04-08T00:00:00",
          "2016-04-11T00:00:00",
          "2016-04-12T00:00:00",
          "2016-04-13T00:00:00",
          "2016-04-14T00:00:00",
          "2016-04-15T00:00:00",
          "2016-04-18T00:00:00",
          "2016-04-19T00:00:00",
          "2016-04-20T00:00:00",
          "2016-04-21T00:00:00",
          "2016-04-22T00:00:00",
          "2016-04-25T00:00:00",
          "2016-04-26T00:00:00",
          "2016-04-27T00:00:00",
          "2016-04-28T00:00:00",
          "2016-04-29T00:00:00",
          "2016-05-02T00:00:00",
          "2016-05-03T00:00:00",
          "2016-05-04T00:00:00",
          "2016-05-05T00:00:00",
          "2016-05-06T00:00:00",
          "2016-05-09T00:00:00",
          "2016-05-10T00:00:00",
          "2016-05-11T00:00:00",
          "2016-05-12T00:00:00",
          "2016-05-13T00:00:00",
          "2016-05-16T00:00:00",
          "2016-05-17T00:00:00",
          "2016-05-18T00:00:00",
          "2016-05-19T00:00:00",
          "2016-05-20T00:00:00",
          "2016-05-23T00:00:00",
          "2016-05-24T00:00:00",
          "2016-05-25T00:00:00",
          "2016-05-26T00:00:00",
          "2016-05-27T00:00:00",
          "2016-05-31T00:00:00",
          "2016-06-01T00:00:00",
          "2016-06-02T00:00:00",
          "2016-06-03T00:00:00",
          "2016-06-06T00:00:00",
          "2016-06-07T00:00:00",
          "2016-06-08T00:00:00",
          "2016-06-09T00:00:00",
          "2016-06-10T00:00:00",
          "2016-06-13T00:00:00",
          "2016-06-14T00:00:00",
          "2016-06-15T00:00:00",
          "2016-06-16T00:00:00",
          "2016-06-17T00:00:00",
          "2016-06-20T00:00:00",
          "2016-06-21T00:00:00",
          "2016-06-22T00:00:00",
          "2016-06-23T00:00:00",
          "2016-06-24T00:00:00",
          "2016-06-27T00:00:00",
          "2016-06-28T00:00:00",
          "2016-06-29T00:00:00",
          "2016-06-30T00:00:00",
          "2016-07-01T00:00:00",
          "2016-07-05T00:00:00",
          "2016-07-06T00:00:00",
          "2016-07-07T00:00:00",
          "2016-07-08T00:00:00",
          "2016-07-11T00:00:00",
          "2016-07-12T00:00:00",
          "2016-07-13T00:00:00",
          "2016-07-14T00:00:00",
          "2016-07-15T00:00:00",
          "2016-07-18T00:00:00",
          "2016-07-19T00:00:00",
          "2016-07-20T00:00:00",
          "2016-07-21T00:00:00",
          "2016-07-22T00:00:00",
          "2016-07-25T00:00:00",
          "2016-07-26T00:00:00",
          "2016-07-27T00:00:00",
          "2016-07-28T00:00:00",
          "2016-07-29T00:00:00",
          "2016-08-01T00:00:00",
          "2016-08-02T00:00:00",
          "2016-08-03T00:00:00",
          "2016-08-04T00:00:00",
          "2016-08-05T00:00:00",
          "2016-08-08T00:00:00",
          "2016-08-09T00:00:00",
          "2016-08-10T00:00:00",
          "2016-08-11T00:00:00",
          "2016-08-12T00:00:00",
          "2016-08-15T00:00:00",
          "2016-08-16T00:00:00",
          "2016-08-17T00:00:00",
          "2016-08-18T00:00:00",
          "2016-08-19T00:00:00",
          "2016-08-22T00:00:00",
          "2016-08-23T00:00:00",
          "2016-08-24T00:00:00",
          "2016-08-25T00:00:00",
          "2016-08-26T00:00:00",
          "2016-08-29T00:00:00",
          "2016-08-30T00:00:00",
          "2016-08-31T00:00:00",
          "2016-09-01T00:00:00",
          "2016-09-02T00:00:00",
          "2016-09-06T00:00:00",
          "2016-09-07T00:00:00",
          "2016-09-08T00:00:00",
          "2016-09-09T00:00:00",
          "2016-09-12T00:00:00",
          "2016-09-13T00:00:00",
          "2016-09-14T00:00:00",
          "2016-09-15T00:00:00",
          "2016-09-16T00:00:00",
          "2016-09-19T00:00:00",
          "2016-09-20T00:00:00",
          "2016-09-21T00:00:00",
          "2016-09-22T00:00:00",
          "2016-09-23T00:00:00",
          "2016-09-26T00:00:00",
          "2016-09-27T00:00:00",
          "2016-09-28T00:00:00",
          "2016-09-29T00:00:00",
          "2016-09-30T00:00:00",
          "2016-10-03T00:00:00",
          "2016-10-04T00:00:00",
          "2016-10-05T00:00:00",
          "2016-10-06T00:00:00",
          "2016-10-07T00:00:00",
          "2016-10-10T00:00:00",
          "2016-10-11T00:00:00",
          "2016-10-12T00:00:00",
          "2016-10-13T00:00:00",
          "2016-10-14T00:00:00",
          "2016-10-17T00:00:00",
          "2016-10-18T00:00:00",
          "2016-10-19T00:00:00",
          "2016-10-20T00:00:00",
          "2016-10-21T00:00:00",
          "2016-10-24T00:00:00",
          "2016-10-25T00:00:00",
          "2016-10-26T00:00:00",
          "2016-10-27T00:00:00",
          "2016-10-28T00:00:00",
          "2016-10-31T00:00:00",
          "2016-11-01T00:00:00",
          "2016-11-02T00:00:00",
          "2016-11-03T00:00:00",
          "2016-11-04T00:00:00",
          "2016-11-07T00:00:00",
          "2016-11-08T00:00:00",
          "2016-11-09T00:00:00",
          "2016-11-10T00:00:00",
          "2016-11-11T00:00:00",
          "2016-11-14T00:00:00",
          "2016-11-15T00:00:00",
          "2016-11-16T00:00:00",
          "2016-11-17T00:00:00",
          "2016-11-18T00:00:00",
          "2016-11-21T00:00:00",
          "2016-11-22T00:00:00",
          "2016-11-23T00:00:00",
          "2016-11-25T00:00:00",
          "2016-11-28T00:00:00",
          "2016-11-29T00:00:00",
          "2016-11-30T00:00:00",
          "2016-12-01T00:00:00",
          "2016-12-02T00:00:00",
          "2016-12-05T00:00:00",
          "2016-12-06T00:00:00",
          "2016-12-07T00:00:00",
          "2016-12-08T00:00:00",
          "2016-12-09T00:00:00",
          "2016-12-12T00:00:00",
          "2016-12-13T00:00:00",
          "2016-12-14T00:00:00",
          "2016-12-15T00:00:00",
          "2016-12-16T00:00:00",
          "2016-12-19T00:00:00",
          "2016-12-20T00:00:00",
          "2016-12-21T00:00:00",
          "2016-12-22T00:00:00",
          "2016-12-23T00:00:00",
          "2016-12-27T00:00:00",
          "2016-12-28T00:00:00",
          "2016-12-29T00:00:00",
          "2016-12-30T00:00:00",
          "2017-01-03T00:00:00",
          "2017-01-04T00:00:00",
          "2017-01-05T00:00:00",
          "2017-01-06T00:00:00",
          "2017-01-09T00:00:00",
          "2017-01-10T00:00:00",
          "2017-01-11T00:00:00",
          "2017-01-12T00:00:00",
          "2017-01-13T00:00:00",
          "2017-01-17T00:00:00",
          "2017-01-18T00:00:00",
          "2017-01-19T00:00:00",
          "2017-01-20T00:00:00",
          "2017-01-23T00:00:00",
          "2017-01-24T00:00:00",
          "2017-01-25T00:00:00",
          "2017-01-26T00:00:00",
          "2017-01-27T00:00:00",
          "2017-01-30T00:00:00",
          "2017-01-31T00:00:00",
          "2017-02-01T00:00:00",
          "2017-02-02T00:00:00",
          "2017-02-03T00:00:00",
          "2017-02-06T00:00:00",
          "2017-02-07T00:00:00",
          "2017-02-08T00:00:00",
          "2017-02-09T00:00:00",
          "2017-02-10T00:00:00",
          "2017-02-13T00:00:00",
          "2017-02-14T00:00:00",
          "2017-02-15T00:00:00",
          "2017-02-16T00:00:00",
          "2017-02-17T00:00:00",
          "2017-02-21T00:00:00",
          "2017-02-22T00:00:00",
          "2017-02-23T00:00:00",
          "2017-02-24T00:00:00",
          "2017-02-27T00:00:00",
          "2017-02-28T00:00:00",
          "2017-03-01T00:00:00",
          "2017-03-02T00:00:00",
          "2017-03-03T00:00:00",
          "2017-03-06T00:00:00",
          "2017-03-07T00:00:00",
          "2017-03-08T00:00:00",
          "2017-03-09T00:00:00",
          "2017-03-10T00:00:00",
          "2017-03-13T00:00:00",
          "2017-03-14T00:00:00",
          "2017-03-15T00:00:00",
          "2017-03-16T00:00:00",
          "2017-03-17T00:00:00",
          "2017-03-20T00:00:00",
          "2017-03-21T00:00:00",
          "2017-03-22T00:00:00",
          "2017-03-23T00:00:00",
          "2017-03-24T00:00:00",
          "2017-03-27T00:00:00",
          "2017-03-28T00:00:00",
          "2017-03-29T00:00:00",
          "2017-03-30T00:00:00",
          "2017-03-31T00:00:00",
          "2017-04-03T00:00:00",
          "2017-04-04T00:00:00",
          "2017-04-05T00:00:00",
          "2017-04-06T00:00:00",
          "2017-04-07T00:00:00",
          "2017-04-10T00:00:00",
          "2017-04-11T00:00:00",
          "2017-04-12T00:00:00",
          "2017-04-13T00:00:00",
          "2017-04-17T00:00:00",
          "2017-04-18T00:00:00",
          "2017-04-19T00:00:00",
          "2017-04-20T00:00:00",
          "2017-04-21T00:00:00",
          "2017-04-24T00:00:00",
          "2017-04-25T00:00:00",
          "2017-04-26T00:00:00",
          "2017-04-27T00:00:00",
          "2017-04-28T00:00:00",
          "2017-05-01T00:00:00",
          "2017-05-02T00:00:00",
          "2017-05-03T00:00:00",
          "2017-05-04T00:00:00",
          "2017-05-05T00:00:00",
          "2017-05-08T00:00:00",
          "2017-05-09T00:00:00",
          "2017-05-10T00:00:00",
          "2017-05-11T00:00:00",
          "2017-05-12T00:00:00",
          "2017-05-15T00:00:00",
          "2017-05-16T00:00:00",
          "2017-05-17T00:00:00",
          "2017-05-18T00:00:00",
          "2017-05-19T00:00:00",
          "2017-05-22T00:00:00",
          "2017-05-23T00:00:00",
          "2017-05-24T00:00:00",
          "2017-05-25T00:00:00",
          "2017-05-26T00:00:00",
          "2017-05-30T00:00:00",
          "2017-05-31T00:00:00",
          "2017-06-01T00:00:00",
          "2017-06-02T00:00:00",
          "2017-06-05T00:00:00",
          "2017-06-06T00:00:00",
          "2017-06-07T00:00:00",
          "2017-06-08T00:00:00",
          "2017-06-09T00:00:00",
          "2017-06-12T00:00:00",
          "2017-06-13T00:00:00",
          "2017-06-14T00:00:00",
          "2017-06-15T00:00:00",
          "2017-06-16T00:00:00",
          "2017-06-19T00:00:00",
          "2017-06-20T00:00:00",
          "2017-06-21T00:00:00",
          "2017-06-22T00:00:00",
          "2017-06-23T00:00:00",
          "2017-06-26T00:00:00",
          "2017-06-27T00:00:00",
          "2017-06-28T00:00:00",
          "2017-06-29T00:00:00",
          "2017-06-30T00:00:00",
          "2017-07-03T00:00:00",
          "2017-07-05T00:00:00",
          "2017-07-06T00:00:00",
          "2017-07-07T00:00:00",
          "2017-07-10T00:00:00",
          "2017-07-11T00:00:00",
          "2017-07-12T00:00:00",
          "2017-07-13T00:00:00",
          "2017-07-14T00:00:00",
          "2017-07-17T00:00:00",
          "2017-07-18T00:00:00",
          "2017-07-19T00:00:00",
          "2017-07-20T00:00:00",
          "2017-07-21T00:00:00",
          "2017-07-24T00:00:00",
          "2017-07-25T00:00:00",
          "2017-07-26T00:00:00",
          "2017-07-27T00:00:00",
          "2017-07-28T00:00:00",
          "2017-07-31T00:00:00",
          "2017-08-01T00:00:00",
          "2017-08-02T00:00:00",
          "2017-08-03T00:00:00",
          "2017-08-04T00:00:00",
          "2017-08-07T00:00:00",
          "2017-08-08T00:00:00",
          "2017-08-09T00:00:00",
          "2017-08-10T00:00:00",
          "2017-08-11T00:00:00",
          "2017-08-14T00:00:00",
          "2017-08-15T00:00:00",
          "2017-08-16T00:00:00",
          "2017-08-17T00:00:00",
          "2017-08-18T00:00:00",
          "2017-08-21T00:00:00",
          "2017-08-22T00:00:00",
          "2017-08-23T00:00:00",
          "2017-08-24T00:00:00",
          "2017-08-25T00:00:00",
          "2017-08-28T00:00:00",
          "2017-08-29T00:00:00",
          "2017-08-30T00:00:00",
          "2017-08-31T00:00:00",
          "2017-09-01T00:00:00",
          "2017-09-05T00:00:00",
          "2017-09-06T00:00:00",
          "2017-09-07T00:00:00",
          "2017-09-08T00:00:00",
          "2017-09-11T00:00:00",
          "2017-09-12T00:00:00",
          "2017-09-13T00:00:00",
          "2017-09-14T00:00:00",
          "2017-09-15T00:00:00",
          "2017-09-18T00:00:00",
          "2017-09-19T00:00:00",
          "2017-09-20T00:00:00",
          "2017-09-21T00:00:00",
          "2017-09-22T00:00:00",
          "2017-09-25T00:00:00",
          "2017-09-26T00:00:00",
          "2017-09-27T00:00:00",
          "2017-09-28T00:00:00",
          "2017-09-29T00:00:00",
          "2017-10-02T00:00:00",
          "2017-10-03T00:00:00",
          "2017-10-04T00:00:00",
          "2017-10-05T00:00:00",
          "2017-10-06T00:00:00",
          "2017-10-09T00:00:00",
          "2017-10-10T00:00:00",
          "2017-10-11T00:00:00",
          "2017-10-12T00:00:00",
          "2017-10-13T00:00:00",
          "2017-10-16T00:00:00",
          "2017-10-17T00:00:00",
          "2017-10-18T00:00:00",
          "2017-10-19T00:00:00",
          "2017-10-20T00:00:00",
          "2017-10-23T00:00:00",
          "2017-10-24T00:00:00",
          "2017-10-25T00:00:00",
          "2017-10-26T00:00:00",
          "2017-10-27T00:00:00",
          "2017-10-30T00:00:00",
          "2017-10-31T00:00:00",
          "2017-11-01T00:00:00",
          "2017-11-02T00:00:00",
          "2017-11-03T00:00:00",
          "2017-11-06T00:00:00",
          "2017-11-07T00:00:00",
          "2017-11-08T00:00:00",
          "2017-11-09T00:00:00",
          "2017-11-10T00:00:00",
          "2017-11-13T00:00:00",
          "2017-11-14T00:00:00",
          "2017-11-15T00:00:00",
          "2017-11-16T00:00:00",
          "2017-11-17T00:00:00",
          "2017-11-20T00:00:00",
          "2017-11-21T00:00:00",
          "2017-11-22T00:00:00",
          "2017-11-24T00:00:00",
          "2017-11-27T00:00:00",
          "2017-11-28T00:00:00",
          "2017-11-29T00:00:00",
          "2017-11-30T00:00:00",
          "2017-12-01T00:00:00",
          "2017-12-04T00:00:00",
          "2017-12-05T00:00:00",
          "2017-12-06T00:00:00",
          "2017-12-07T00:00:00",
          "2017-12-08T00:00:00",
          "2017-12-11T00:00:00",
          "2017-12-12T00:00:00",
          "2017-12-13T00:00:00",
          "2017-12-14T00:00:00",
          "2017-12-15T00:00:00",
          "2017-12-18T00:00:00",
          "2017-12-19T00:00:00",
          "2017-12-20T00:00:00",
          "2017-12-21T00:00:00",
          "2017-12-22T00:00:00",
          "2017-12-26T00:00:00",
          "2017-12-27T00:00:00",
          "2017-12-28T00:00:00",
          "2017-12-29T00:00:00",
          "2018-01-02T00:00:00",
          "2018-01-03T00:00:00",
          "2018-01-04T00:00:00",
          "2018-01-05T00:00:00",
          "2018-01-08T00:00:00",
          "2018-01-09T00:00:00",
          "2018-01-10T00:00:00",
          "2018-01-11T00:00:00",
          "2018-01-12T00:00:00",
          "2018-01-16T00:00:00",
          "2018-01-17T00:00:00",
          "2018-01-18T00:00:00",
          "2018-01-19T00:00:00",
          "2018-01-22T00:00:00",
          "2018-01-23T00:00:00",
          "2018-01-24T00:00:00",
          "2018-01-25T00:00:00",
          "2018-01-26T00:00:00",
          "2018-01-29T00:00:00",
          "2018-01-30T00:00:00",
          "2018-01-31T00:00:00",
          "2018-02-01T00:00:00",
          "2018-02-02T00:00:00",
          "2018-02-05T00:00:00",
          "2018-02-06T00:00:00",
          "2018-02-07T00:00:00",
          "2018-02-08T00:00:00",
          "2018-02-09T00:00:00",
          "2018-02-12T00:00:00",
          "2018-02-13T00:00:00",
          "2018-02-14T00:00:00",
          "2018-02-15T00:00:00",
          "2018-02-16T00:00:00",
          "2018-02-20T00:00:00",
          "2018-02-21T00:00:00",
          "2018-02-22T00:00:00",
          "2018-02-23T00:00:00",
          "2018-02-26T00:00:00",
          "2018-02-27T00:00:00",
          "2018-02-28T00:00:00",
          "2018-03-01T00:00:00",
          "2018-03-02T00:00:00",
          "2018-03-05T00:00:00",
          "2018-03-06T00:00:00",
          "2018-03-07T00:00:00",
          "2018-03-08T00:00:00",
          "2018-03-09T00:00:00",
          "2018-03-12T00:00:00",
          "2018-03-13T00:00:00",
          "2018-03-14T00:00:00",
          "2018-03-15T00:00:00",
          "2018-03-16T00:00:00",
          "2018-03-19T00:00:00",
          "2018-03-20T00:00:00",
          "2018-03-21T00:00:00",
          "2018-03-22T00:00:00",
          "2018-03-23T00:00:00",
          "2018-03-26T00:00:00",
          "2018-03-27T00:00:00",
          "2018-03-28T00:00:00",
          "2018-03-29T00:00:00",
          "2018-04-02T00:00:00",
          "2018-04-03T00:00:00",
          "2018-04-04T00:00:00",
          "2018-04-05T00:00:00",
          "2018-04-06T00:00:00",
          "2018-04-09T00:00:00",
          "2018-04-10T00:00:00",
          "2018-04-11T00:00:00",
          "2018-04-12T00:00:00",
          "2018-04-13T00:00:00",
          "2018-04-16T00:00:00",
          "2018-04-17T00:00:00",
          "2018-04-18T00:00:00",
          "2018-04-19T00:00:00",
          "2018-04-20T00:00:00",
          "2018-04-23T00:00:00",
          "2018-04-24T00:00:00",
          "2018-04-25T00:00:00",
          "2018-04-26T00:00:00",
          "2018-04-27T00:00:00",
          "2018-04-30T00:00:00",
          "2018-05-01T00:00:00",
          "2018-05-02T00:00:00",
          "2018-05-03T00:00:00",
          "2018-05-04T00:00:00",
          "2018-05-07T00:00:00",
          "2018-05-08T00:00:00",
          "2018-05-09T00:00:00",
          "2018-05-10T00:00:00",
          "2018-05-11T00:00:00",
          "2018-05-14T00:00:00",
          "2018-05-15T00:00:00",
          "2018-05-16T00:00:00",
          "2018-05-17T00:00:00",
          "2018-05-18T00:00:00",
          "2018-05-21T00:00:00",
          "2018-05-22T00:00:00",
          "2018-05-23T00:00:00",
          "2018-05-24T00:00:00",
          "2018-05-25T00:00:00",
          "2018-05-29T00:00:00",
          "2018-05-30T00:00:00",
          "2018-05-31T00:00:00",
          "2018-06-01T00:00:00",
          "2018-06-04T00:00:00",
          "2018-06-05T00:00:00",
          "2018-06-06T00:00:00",
          "2018-06-07T00:00:00",
          "2018-06-08T00:00:00",
          "2018-06-11T00:00:00",
          "2018-06-12T00:00:00",
          "2018-06-13T00:00:00",
          "2018-06-14T00:00:00",
          "2018-06-15T00:00:00",
          "2018-06-18T00:00:00",
          "2018-06-19T00:00:00",
          "2018-06-20T00:00:00",
          "2018-06-21T00:00:00",
          "2018-06-22T00:00:00",
          "2018-06-25T00:00:00",
          "2018-06-26T00:00:00",
          "2018-06-27T00:00:00",
          "2018-06-28T00:00:00",
          "2018-06-29T00:00:00",
          "2018-07-02T00:00:00",
          "2018-07-03T00:00:00",
          "2018-07-05T00:00:00",
          "2018-07-06T00:00:00",
          "2018-07-09T00:00:00",
          "2018-07-10T00:00:00",
          "2018-07-11T00:00:00",
          "2018-07-12T00:00:00",
          "2018-07-13T00:00:00",
          "2018-07-16T00:00:00",
          "2018-07-17T00:00:00",
          "2018-07-18T00:00:00",
          "2018-07-19T00:00:00",
          "2018-07-20T00:00:00",
          "2018-07-23T00:00:00",
          "2018-07-24T00:00:00",
          "2018-07-25T00:00:00",
          "2018-07-26T00:00:00",
          "2018-07-27T00:00:00",
          "2018-07-30T00:00:00",
          "2018-07-31T00:00:00",
          "2018-08-01T00:00:00",
          "2018-08-02T00:00:00",
          "2018-08-03T00:00:00",
          "2018-08-06T00:00:00",
          "2018-08-07T00:00:00",
          "2018-08-08T00:00:00",
          "2018-08-09T00:00:00",
          "2018-08-10T00:00:00",
          "2018-08-13T00:00:00",
          "2018-08-14T00:00:00",
          "2018-08-15T00:00:00",
          "2018-08-16T00:00:00",
          "2018-08-17T00:00:00",
          "2018-08-20T00:00:00",
          "2018-08-21T00:00:00",
          "2018-08-22T00:00:00",
          "2018-08-23T00:00:00",
          "2018-08-24T00:00:00",
          "2018-08-27T00:00:00",
          "2018-08-28T00:00:00",
          "2018-08-29T00:00:00",
          "2018-08-30T00:00:00",
          "2018-08-31T00:00:00",
          "2018-09-04T00:00:00",
          "2018-09-05T00:00:00",
          "2018-09-06T00:00:00",
          "2018-09-07T00:00:00",
          "2018-09-10T00:00:00",
          "2018-09-11T00:00:00",
          "2018-09-12T00:00:00",
          "2018-09-13T00:00:00",
          "2018-09-14T00:00:00",
          "2018-09-17T00:00:00",
          "2018-09-18T00:00:00",
          "2018-09-19T00:00:00",
          "2018-09-20T00:00:00",
          "2018-09-21T00:00:00",
          "2018-09-24T00:00:00",
          "2018-09-25T00:00:00",
          "2018-09-26T00:00:00",
          "2018-09-27T00:00:00",
          "2018-09-28T00:00:00",
          "2018-10-01T00:00:00",
          "2018-10-02T00:00:00",
          "2018-10-03T00:00:00",
          "2018-10-04T00:00:00",
          "2018-10-05T00:00:00",
          "2018-10-08T00:00:00",
          "2018-10-09T00:00:00",
          "2018-10-10T00:00:00",
          "2018-10-11T00:00:00",
          "2018-10-12T00:00:00",
          "2018-10-15T00:00:00",
          "2018-10-16T00:00:00",
          "2018-10-17T00:00:00",
          "2018-10-18T00:00:00",
          "2018-10-19T00:00:00",
          "2018-10-22T00:00:00",
          "2018-10-23T00:00:00",
          "2018-10-24T00:00:00",
          "2018-10-25T00:00:00",
          "2018-10-26T00:00:00",
          "2018-10-29T00:00:00",
          "2018-10-30T00:00:00",
          "2018-10-31T00:00:00",
          "2018-11-01T00:00:00",
          "2018-11-02T00:00:00",
          "2018-11-05T00:00:00",
          "2018-11-06T00:00:00",
          "2018-11-07T00:00:00",
          "2018-11-08T00:00:00",
          "2018-11-09T00:00:00",
          "2018-11-12T00:00:00",
          "2018-11-13T00:00:00",
          "2018-11-14T00:00:00",
          "2018-11-15T00:00:00",
          "2018-11-16T00:00:00",
          "2018-11-19T00:00:00",
          "2018-11-20T00:00:00",
          "2018-11-21T00:00:00",
          "2018-11-23T00:00:00",
          "2018-11-26T00:00:00",
          "2018-11-27T00:00:00",
          "2018-11-28T00:00:00",
          "2018-11-29T00:00:00",
          "2018-11-30T00:00:00",
          "2018-12-03T00:00:00",
          "2018-12-04T00:00:00",
          "2018-12-06T00:00:00",
          "2018-12-07T00:00:00",
          "2018-12-10T00:00:00",
          "2018-12-11T00:00:00",
          "2018-12-12T00:00:00",
          "2018-12-13T00:00:00",
          "2018-12-14T00:00:00",
          "2018-12-17T00:00:00",
          "2018-12-18T00:00:00",
          "2018-12-19T00:00:00",
          "2018-12-20T00:00:00",
          "2018-12-21T00:00:00",
          "2018-12-24T00:00:00",
          "2018-12-26T00:00:00",
          "2018-12-27T00:00:00",
          "2018-12-28T00:00:00",
          "2018-12-31T00:00:00",
          "2019-01-02T00:00:00",
          "2019-01-03T00:00:00",
          "2019-01-04T00:00:00",
          "2019-01-07T00:00:00",
          "2019-01-08T00:00:00",
          "2019-01-09T00:00:00",
          "2019-01-10T00:00:00",
          "2019-01-11T00:00:00",
          "2019-01-14T00:00:00",
          "2019-01-15T00:00:00",
          "2019-01-16T00:00:00",
          "2019-01-17T00:00:00",
          "2019-01-18T00:00:00",
          "2019-01-22T00:00:00",
          "2019-01-23T00:00:00",
          "2019-01-24T00:00:00",
          "2019-01-25T00:00:00",
          "2019-01-28T00:00:00",
          "2019-01-29T00:00:00",
          "2019-01-30T00:00:00",
          "2019-01-31T00:00:00",
          "2019-02-01T00:00:00",
          "2019-02-04T00:00:00",
          "2019-02-05T00:00:00",
          "2019-02-06T00:00:00",
          "2019-02-07T00:00:00",
          "2019-02-08T00:00:00",
          "2019-02-11T00:00:00",
          "2019-02-12T00:00:00",
          "2019-02-13T00:00:00",
          "2019-02-14T00:00:00",
          "2019-02-15T00:00:00",
          "2019-02-19T00:00:00",
          "2019-02-20T00:00:00",
          "2019-02-21T00:00:00",
          "2019-02-22T00:00:00",
          "2019-02-25T00:00:00",
          "2019-02-26T00:00:00",
          "2019-02-27T00:00:00",
          "2019-02-28T00:00:00",
          "2019-03-01T00:00:00",
          "2019-03-04T00:00:00",
          "2019-03-05T00:00:00",
          "2019-03-06T00:00:00",
          "2019-03-07T00:00:00",
          "2019-03-08T00:00:00",
          "2019-03-11T00:00:00",
          "2019-03-12T00:00:00",
          "2019-03-13T00:00:00",
          "2019-03-14T00:00:00",
          "2019-03-15T00:00:00",
          "2019-03-18T00:00:00",
          "2019-03-19T00:00:00",
          "2019-03-20T00:00:00",
          "2019-03-21T00:00:00",
          "2019-03-22T00:00:00",
          "2019-03-25T00:00:00",
          "2019-03-26T00:00:00",
          "2019-03-27T00:00:00",
          "2019-03-28T00:00:00",
          "2019-03-29T00:00:00",
          "2019-04-01T00:00:00",
          "2019-04-02T00:00:00",
          "2019-04-03T00:00:00",
          "2019-04-04T00:00:00",
          "2019-04-05T00:00:00",
          "2019-04-08T00:00:00",
          "2019-04-09T00:00:00",
          "2019-04-10T00:00:00",
          "2019-04-11T00:00:00",
          "2019-04-12T00:00:00",
          "2019-04-15T00:00:00",
          "2019-04-16T00:00:00",
          "2019-04-17T00:00:00",
          "2019-04-18T00:00:00",
          "2019-04-22T00:00:00",
          "2019-04-23T00:00:00",
          "2019-04-24T00:00:00",
          "2019-04-25T00:00:00",
          "2019-04-26T00:00:00",
          "2019-04-29T00:00:00",
          "2019-04-30T00:00:00",
          "2019-05-01T00:00:00",
          "2019-05-02T00:00:00",
          "2019-05-03T00:00:00",
          "2019-05-06T00:00:00",
          "2019-05-07T00:00:00",
          "2019-05-08T00:00:00",
          "2019-05-09T00:00:00",
          "2019-05-10T00:00:00",
          "2019-05-13T00:00:00",
          "2019-05-14T00:00:00",
          "2019-05-15T00:00:00",
          "2019-05-16T00:00:00",
          "2019-05-17T00:00:00",
          "2019-05-20T00:00:00",
          "2019-05-21T00:00:00",
          "2019-05-22T00:00:00",
          "2019-05-23T00:00:00",
          "2019-05-24T00:00:00",
          "2019-05-28T00:00:00",
          "2019-05-29T00:00:00",
          "2019-05-30T00:00:00",
          "2019-05-31T00:00:00",
          "2019-06-03T00:00:00",
          "2019-06-04T00:00:00",
          "2019-06-05T00:00:00",
          "2019-06-06T00:00:00",
          "2019-06-07T00:00:00",
          "2019-06-10T00:00:00",
          "2019-06-11T00:00:00",
          "2019-06-12T00:00:00",
          "2019-06-13T00:00:00",
          "2019-06-14T00:00:00",
          "2019-06-17T00:00:00",
          "2019-06-18T00:00:00",
          "2019-06-19T00:00:00",
          "2019-06-20T00:00:00",
          "2019-06-21T00:00:00",
          "2019-06-24T00:00:00",
          "2019-06-25T00:00:00",
          "2019-06-26T00:00:00",
          "2019-06-27T00:00:00",
          "2019-06-28T00:00:00",
          "2019-07-01T00:00:00",
          "2019-07-02T00:00:00",
          "2019-07-03T00:00:00",
          "2019-07-05T00:00:00",
          "2019-07-08T00:00:00",
          "2019-07-09T00:00:00",
          "2019-07-10T00:00:00",
          "2019-07-11T00:00:00",
          "2019-07-12T00:00:00",
          "2019-07-15T00:00:00",
          "2019-07-16T00:00:00",
          "2019-07-17T00:00:00",
          "2019-07-18T00:00:00",
          "2019-07-19T00:00:00",
          "2019-07-22T00:00:00",
          "2019-07-23T00:00:00",
          "2019-07-24T00:00:00",
          "2019-07-25T00:00:00",
          "2019-07-26T00:00:00",
          "2019-07-29T00:00:00",
          "2019-07-30T00:00:00",
          "2019-07-31T00:00:00",
          "2019-08-01T00:00:00",
          "2019-08-02T00:00:00",
          "2019-08-05T00:00:00",
          "2019-08-06T00:00:00",
          "2019-08-07T00:00:00",
          "2019-08-08T00:00:00",
          "2019-08-09T00:00:00",
          "2019-08-12T00:00:00",
          "2019-08-13T00:00:00",
          "2019-08-14T00:00:00",
          "2019-08-15T00:00:00",
          "2019-08-16T00:00:00",
          "2019-08-19T00:00:00",
          "2019-08-20T00:00:00",
          "2019-08-21T00:00:00",
          "2019-08-22T00:00:00",
          "2019-08-23T00:00:00",
          "2019-08-26T00:00:00",
          "2019-08-27T00:00:00",
          "2019-08-28T00:00:00",
          "2019-08-29T00:00:00",
          "2019-08-30T00:00:00",
          "2019-09-03T00:00:00",
          "2019-09-04T00:00:00",
          "2019-09-05T00:00:00",
          "2019-09-06T00:00:00",
          "2019-09-09T00:00:00",
          "2019-09-10T00:00:00",
          "2019-09-11T00:00:00",
          "2019-09-12T00:00:00",
          "2019-09-13T00:00:00",
          "2019-09-16T00:00:00",
          "2019-09-17T00:00:00",
          "2019-09-18T00:00:00",
          "2019-09-19T00:00:00",
          "2019-09-20T00:00:00",
          "2019-09-23T00:00:00",
          "2019-09-24T00:00:00",
          "2019-09-25T00:00:00",
          "2019-09-26T00:00:00",
          "2019-09-27T00:00:00",
          "2019-09-30T00:00:00",
          "2019-10-01T00:00:00",
          "2019-10-02T00:00:00",
          "2019-10-03T00:00:00",
          "2019-10-04T00:00:00",
          "2019-10-07T00:00:00",
          "2019-10-08T00:00:00",
          "2019-10-09T00:00:00",
          "2019-10-10T00:00:00",
          "2019-10-11T00:00:00",
          "2019-10-14T00:00:00",
          "2019-10-15T00:00:00",
          "2019-10-16T00:00:00",
          "2019-10-17T00:00:00",
          "2019-10-18T00:00:00",
          "2019-10-21T00:00:00",
          "2019-10-22T00:00:00",
          "2019-10-23T00:00:00",
          "2019-10-24T00:00:00",
          "2019-10-25T00:00:00",
          "2019-10-28T00:00:00",
          "2019-10-29T00:00:00",
          "2019-10-30T00:00:00",
          "2019-10-31T00:00:00",
          "2019-11-01T00:00:00",
          "2019-11-04T00:00:00",
          "2019-11-05T00:00:00",
          "2019-11-06T00:00:00",
          "2019-11-07T00:00:00",
          "2019-11-08T00:00:00",
          "2019-11-11T00:00:00",
          "2019-11-12T00:00:00",
          "2019-11-13T00:00:00",
          "2019-11-14T00:00:00",
          "2019-11-15T00:00:00",
          "2019-11-18T00:00:00",
          "2019-11-19T00:00:00",
          "2019-11-20T00:00:00",
          "2019-11-21T00:00:00",
          "2019-11-22T00:00:00",
          "2019-11-25T00:00:00",
          "2019-11-26T00:00:00",
          "2019-11-27T00:00:00",
          "2019-11-29T00:00:00",
          "2019-12-02T00:00:00",
          "2019-12-03T00:00:00",
          "2019-12-04T00:00:00",
          "2019-12-05T00:00:00",
          "2019-12-06T00:00:00",
          "2019-12-09T00:00:00",
          "2019-12-10T00:00:00",
          "2019-12-11T00:00:00",
          "2019-12-12T00:00:00",
          "2019-12-13T00:00:00",
          "2019-12-16T00:00:00",
          "2019-12-17T00:00:00",
          "2019-12-18T00:00:00",
          "2019-12-19T00:00:00",
          "2019-12-20T00:00:00",
          "2019-12-23T00:00:00",
          "2019-12-24T00:00:00",
          "2019-12-26T00:00:00",
          "2019-12-27T00:00:00",
          "2019-12-30T00:00:00",
          "2019-12-31T00:00:00",
          "2020-01-02T00:00:00",
          "2020-01-03T00:00:00",
          "2020-01-06T00:00:00",
          "2020-01-07T00:00:00",
          "2020-01-08T00:00:00",
          "2020-01-09T00:00:00",
          "2020-01-10T00:00:00",
          "2020-01-13T00:00:00",
          "2020-01-14T00:00:00",
          "2020-01-15T00:00:00",
          "2020-01-16T00:00:00",
          "2020-01-17T00:00:00",
          "2020-01-21T00:00:00",
          "2020-01-22T00:00:00",
          "2020-01-23T00:00:00",
          "2020-01-24T00:00:00",
          "2020-01-27T00:00:00",
          "2020-01-28T00:00:00",
          "2020-01-29T00:00:00",
          "2020-01-30T00:00:00",
          "2020-01-31T00:00:00",
          "2020-02-03T00:00:00",
          "2020-02-04T00:00:00",
          "2020-02-05T00:00:00",
          "2020-02-06T00:00:00",
          "2020-02-07T00:00:00",
          "2020-02-10T00:00:00",
          "2020-02-11T00:00:00",
          "2020-02-12T00:00:00",
          "2020-02-13T00:00:00",
          "2020-02-14T00:00:00",
          "2020-02-18T00:00:00",
          "2020-02-19T00:00:00",
          "2020-02-20T00:00:00",
          "2020-02-21T00:00:00",
          "2020-02-24T00:00:00",
          "2020-02-25T00:00:00",
          "2020-02-26T00:00:00",
          "2020-02-27T00:00:00",
          "2020-02-28T00:00:00",
          "2020-03-02T00:00:00",
          "2020-03-03T00:00:00",
          "2020-03-04T00:00:00",
          "2020-03-05T00:00:00",
          "2020-03-06T00:00:00",
          "2020-03-09T00:00:00",
          "2020-03-10T00:00:00",
          "2020-03-11T00:00:00",
          "2020-03-12T00:00:00",
          "2020-03-13T00:00:00",
          "2020-03-16T00:00:00",
          "2020-03-17T00:00:00",
          "2020-03-18T00:00:00",
          "2020-03-19T00:00:00",
          "2020-03-20T00:00:00",
          "2020-03-23T00:00:00",
          "2020-03-24T00:00:00",
          "2020-03-25T00:00:00",
          "2020-03-26T00:00:00",
          "2020-03-27T00:00:00",
          "2020-03-30T00:00:00",
          "2020-03-31T00:00:00",
          "2020-04-01T00:00:00",
          "2020-04-02T00:00:00",
          "2020-04-03T00:00:00",
          "2020-04-06T00:00:00",
          "2020-04-07T00:00:00",
          "2020-04-08T00:00:00",
          "2020-04-09T00:00:00",
          "2020-04-13T00:00:00",
          "2020-04-14T00:00:00",
          "2020-04-15T00:00:00",
          "2020-04-16T00:00:00",
          "2020-04-17T00:00:00",
          "2020-04-20T00:00:00",
          "2020-04-21T00:00:00",
          "2020-04-22T00:00:00",
          "2020-04-23T00:00:00",
          "2020-04-24T00:00:00",
          "2020-04-27T00:00:00",
          "2020-04-28T00:00:00",
          "2020-04-29T00:00:00",
          "2020-04-30T00:00:00",
          "2020-05-01T00:00:00",
          "2020-05-04T00:00:00",
          "2020-05-05T00:00:00",
          "2020-05-06T00:00:00",
          "2020-05-07T00:00:00",
          "2020-05-08T00:00:00",
          "2020-05-11T00:00:00",
          "2020-05-12T00:00:00",
          "2020-05-13T00:00:00",
          "2020-05-14T00:00:00",
          "2020-05-15T00:00:00",
          "2020-05-18T00:00:00",
          "2020-05-19T00:00:00",
          "2020-05-20T00:00:00",
          "2020-05-21T00:00:00",
          "2020-05-22T00:00:00",
          "2020-05-26T00:00:00",
          "2020-05-27T00:00:00",
          "2020-05-28T00:00:00",
          "2020-05-29T00:00:00",
          "2020-06-01T00:00:00",
          "2020-06-02T00:00:00",
          "2020-06-03T00:00:00",
          "2020-06-04T00:00:00",
          "2020-06-05T00:00:00",
          "2020-06-08T00:00:00",
          "2020-06-09T00:00:00",
          "2020-06-10T00:00:00",
          "2020-06-11T00:00:00",
          "2020-06-12T00:00:00",
          "2020-06-15T00:00:00",
          "2020-06-16T00:00:00",
          "2020-06-17T00:00:00",
          "2020-06-18T00:00:00",
          "2020-06-19T00:00:00",
          "2020-06-22T00:00:00",
          "2020-06-23T00:00:00",
          "2020-06-24T00:00:00",
          "2020-06-25T00:00:00",
          "2020-06-26T00:00:00",
          "2020-06-29T00:00:00",
          "2020-06-30T00:00:00",
          "2020-07-01T00:00:00",
          "2020-07-02T00:00:00",
          "2020-07-06T00:00:00",
          "2020-07-07T00:00:00",
          "2020-07-08T00:00:00",
          "2020-07-09T00:00:00",
          "2020-07-10T00:00:00",
          "2020-07-13T00:00:00",
          "2020-07-14T00:00:00",
          "2020-07-15T00:00:00",
          "2020-07-16T00:00:00",
          "2020-07-17T00:00:00",
          "2020-07-20T00:00:00",
          "2020-07-21T00:00:00",
          "2020-07-22T00:00:00",
          "2020-07-23T00:00:00",
          "2020-07-24T00:00:00",
          "2020-07-27T00:00:00",
          "2020-07-28T00:00:00",
          "2020-07-29T00:00:00",
          "2020-07-30T00:00:00",
          "2020-07-31T00:00:00",
          "2020-08-03T00:00:00",
          "2020-08-04T00:00:00",
          "2020-08-05T00:00:00",
          "2020-08-06T00:00:00",
          "2020-08-07T00:00:00",
          "2020-08-10T00:00:00",
          "2020-08-11T00:00:00",
          "2020-08-12T00:00:00",
          "2020-08-13T00:00:00",
          "2020-08-14T00:00:00",
          "2020-08-17T00:00:00",
          "2020-08-18T00:00:00",
          "2020-08-19T00:00:00",
          "2020-08-20T00:00:00",
          "2020-08-21T00:00:00",
          "2020-08-24T00:00:00",
          "2020-08-25T00:00:00",
          "2020-08-26T00:00:00",
          "2020-08-27T00:00:00",
          "2020-08-28T00:00:00",
          "2020-08-31T00:00:00",
          "2020-09-01T00:00:00",
          "2020-09-02T00:00:00",
          "2020-09-03T00:00:00",
          "2020-09-04T00:00:00",
          "2020-09-08T00:00:00",
          "2020-09-09T00:00:00",
          "2020-09-10T00:00:00",
          "2020-09-11T00:00:00",
          "2020-09-14T00:00:00",
          "2020-09-15T00:00:00",
          "2020-09-16T00:00:00",
          "2020-09-17T00:00:00",
          "2020-09-18T00:00:00",
          "2020-09-21T00:00:00",
          "2020-09-22T00:00:00",
          "2020-09-23T00:00:00",
          "2020-09-24T00:00:00",
          "2020-09-25T00:00:00",
          "2020-09-28T00:00:00",
          "2020-09-29T00:00:00",
          "2020-09-30T00:00:00",
          "2020-10-01T00:00:00",
          "2020-10-02T00:00:00",
          "2020-10-05T00:00:00",
          "2020-10-06T00:00:00",
          "2020-10-07T00:00:00",
          "2020-10-08T00:00:00",
          "2020-10-09T00:00:00",
          "2020-10-12T00:00:00",
          "2020-10-13T00:00:00",
          "2020-10-14T00:00:00",
          "2020-10-15T00:00:00",
          "2020-10-16T00:00:00",
          "2020-10-19T00:00:00",
          "2020-10-20T00:00:00",
          "2020-10-21T00:00:00",
          "2020-10-22T00:00:00",
          "2020-10-23T00:00:00",
          "2020-10-26T00:00:00",
          "2020-10-27T00:00:00",
          "2020-10-28T00:00:00",
          "2020-10-29T00:00:00",
          "2020-10-30T00:00:00",
          "2020-11-02T00:00:00",
          "2020-11-03T00:00:00",
          "2020-11-04T00:00:00",
          "2020-11-05T00:00:00",
          "2020-11-06T00:00:00",
          "2020-11-09T00:00:00",
          "2020-11-10T00:00:00",
          "2020-11-11T00:00:00",
          "2020-11-12T00:00:00",
          "2020-11-13T00:00:00",
          "2020-11-16T00:00:00",
          "2020-11-17T00:00:00",
          "2020-11-18T00:00:00",
          "2020-11-19T00:00:00",
          "2020-11-20T00:00:00",
          "2020-11-23T00:00:00",
          "2020-11-24T00:00:00",
          "2020-11-25T00:00:00",
          "2020-11-27T00:00:00",
          "2020-11-30T00:00:00",
          "2020-12-01T00:00:00",
          "2020-12-02T00:00:00",
          "2020-12-03T00:00:00",
          "2020-12-04T00:00:00",
          "2020-12-07T00:00:00",
          "2020-12-08T00:00:00",
          "2020-12-09T00:00:00",
          "2020-12-10T00:00:00",
          "2020-12-11T00:00:00",
          "2020-12-14T00:00:00",
          "2020-12-15T00:00:00",
          "2020-12-16T00:00:00",
          "2020-12-17T00:00:00",
          "2020-12-18T00:00:00",
          "2020-12-21T00:00:00",
          "2020-12-22T00:00:00",
          "2020-12-23T00:00:00",
          "2020-12-24T00:00:00",
          "2020-12-28T00:00:00",
          "2020-12-29T00:00:00",
          "2020-12-30T00:00:00",
          "2020-12-31T00:00:00",
          "2021-01-04T00:00:00",
          "2021-01-05T00:00:00",
          "2021-01-06T00:00:00",
          "2021-01-07T00:00:00",
          "2021-01-08T00:00:00",
          "2021-01-11T00:00:00",
          "2021-01-12T00:00:00",
          "2021-01-13T00:00:00",
          "2021-01-14T00:00:00",
          "2021-01-15T00:00:00",
          "2021-01-19T00:00:00",
          "2021-01-20T00:00:00",
          "2021-01-21T00:00:00",
          "2021-01-22T00:00:00",
          "2021-01-25T00:00:00",
          "2021-01-26T00:00:00",
          "2021-01-27T00:00:00",
          "2021-01-28T00:00:00",
          "2021-01-29T00:00:00",
          "2021-02-01T00:00:00",
          "2021-02-02T00:00:00",
          "2021-02-03T00:00:00",
          "2021-02-04T00:00:00",
          "2021-02-05T00:00:00",
          "2021-02-08T00:00:00",
          "2021-02-09T00:00:00",
          "2021-02-10T00:00:00",
          "2021-02-11T00:00:00",
          "2021-02-12T00:00:00",
          "2021-02-16T00:00:00",
          "2021-02-17T00:00:00",
          "2021-02-18T00:00:00",
          "2021-02-19T00:00:00",
          "2021-02-22T00:00:00",
          "2021-02-23T00:00:00",
          "2021-02-24T00:00:00",
          "2021-02-25T00:00:00",
          "2021-02-26T00:00:00",
          "2021-03-01T00:00:00",
          "2021-03-02T00:00:00",
          "2021-03-03T00:00:00",
          "2021-03-04T00:00:00",
          "2021-03-05T00:00:00",
          "2021-03-08T00:00:00",
          "2021-03-09T00:00:00",
          "2021-03-10T00:00:00",
          "2021-03-11T00:00:00",
          "2021-03-12T00:00:00",
          "2021-03-15T00:00:00",
          "2021-03-16T00:00:00",
          "2021-03-17T00:00:00",
          "2021-03-18T00:00:00",
          "2021-03-19T00:00:00",
          "2021-03-22T00:00:00",
          "2021-03-23T00:00:00",
          "2021-03-24T00:00:00",
          "2021-03-25T00:00:00",
          "2021-03-26T00:00:00",
          "2021-03-29T00:00:00",
          "2021-03-30T00:00:00",
          "2021-03-31T00:00:00",
          "2021-04-01T00:00:00",
          "2021-04-05T00:00:00",
          "2021-04-06T00:00:00",
          "2021-04-07T00:00:00",
          "2021-04-08T00:00:00",
          "2021-04-09T00:00:00",
          "2021-04-12T00:00:00",
          "2021-04-13T00:00:00",
          "2021-04-14T00:00:00",
          "2021-04-15T00:00:00",
          "2021-04-16T00:00:00",
          "2021-04-19T00:00:00",
          "2021-04-20T00:00:00",
          "2021-04-21T00:00:00",
          "2021-04-22T00:00:00",
          "2021-04-23T00:00:00",
          "2021-04-26T00:00:00",
          "2021-04-27T00:00:00",
          "2021-04-28T00:00:00",
          "2021-04-29T00:00:00",
          "2021-04-30T00:00:00",
          "2021-05-03T00:00:00",
          "2021-05-04T00:00:00",
          "2021-05-05T00:00:00",
          "2021-05-06T00:00:00",
          "2021-05-07T00:00:00",
          "2021-05-10T00:00:00",
          "2021-05-11T00:00:00",
          "2021-05-12T00:00:00",
          "2021-05-13T00:00:00",
          "2021-05-14T00:00:00",
          "2021-05-17T00:00:00",
          "2021-05-18T00:00:00",
          "2021-05-19T00:00:00",
          "2021-05-20T00:00:00",
          "2021-05-21T00:00:00",
          "2021-05-24T00:00:00",
          "2021-05-25T00:00:00",
          "2021-05-26T00:00:00",
          "2021-05-27T00:00:00",
          "2021-05-28T00:00:00",
          "2021-06-01T00:00:00",
          "2021-06-02T00:00:00",
          "2021-06-03T00:00:00",
          "2021-06-04T00:00:00",
          "2021-06-07T00:00:00",
          "2021-06-08T00:00:00",
          "2021-06-09T00:00:00",
          "2021-06-10T00:00:00",
          "2021-06-11T00:00:00",
          "2021-06-14T00:00:00",
          "2021-06-15T00:00:00",
          "2021-06-16T00:00:00",
          "2021-06-17T00:00:00",
          "2021-06-18T00:00:00",
          "2021-06-21T00:00:00",
          "2021-06-22T00:00:00",
          "2021-06-23T00:00:00",
          "2021-06-24T00:00:00",
          "2021-06-25T00:00:00",
          "2021-06-28T00:00:00",
          "2021-06-29T00:00:00",
          "2021-06-30T00:00:00",
          "2021-07-01T00:00:00",
          "2021-07-02T00:00:00",
          "2021-07-06T00:00:00",
          "2021-07-07T00:00:00",
          "2021-07-08T00:00:00",
          "2021-07-09T00:00:00",
          "2021-07-12T00:00:00",
          "2021-07-13T00:00:00",
          "2021-07-14T00:00:00",
          "2021-07-15T00:00:00",
          "2021-07-16T00:00:00",
          "2021-07-19T00:00:00",
          "2021-07-20T00:00:00",
          "2021-07-21T00:00:00",
          "2021-07-22T00:00:00",
          "2021-07-23T00:00:00",
          "2021-07-26T00:00:00",
          "2021-07-27T00:00:00",
          "2021-07-28T00:00:00",
          "2021-07-29T00:00:00",
          "2021-07-30T00:00:00",
          "2021-08-02T00:00:00",
          "2021-08-03T00:00:00",
          "2021-08-04T00:00:00",
          "2021-08-05T00:00:00",
          "2021-08-06T00:00:00",
          "2021-08-09T00:00:00",
          "2021-08-10T00:00:00",
          "2021-08-11T00:00:00",
          "2021-08-12T00:00:00",
          "2021-08-13T00:00:00",
          "2021-08-16T00:00:00",
          "2021-08-17T00:00:00",
          "2021-08-18T00:00:00",
          "2021-08-19T00:00:00",
          "2021-08-20T00:00:00",
          "2021-08-23T00:00:00",
          "2021-08-24T00:00:00",
          "2021-08-25T00:00:00",
          "2021-08-26T00:00:00",
          "2021-08-27T00:00:00",
          "2021-08-30T00:00:00",
          "2021-08-31T00:00:00",
          "2021-09-01T00:00:00",
          "2021-09-02T00:00:00",
          "2021-09-03T00:00:00",
          "2021-09-07T00:00:00",
          "2021-09-08T00:00:00",
          "2021-09-09T00:00:00",
          "2021-09-10T00:00:00",
          "2021-09-13T00:00:00",
          "2021-09-14T00:00:00",
          "2021-09-15T00:00:00",
          "2021-09-16T00:00:00",
          "2021-09-17T00:00:00",
          "2021-09-20T00:00:00",
          "2021-09-21T00:00:00",
          "2021-09-22T00:00:00",
          "2021-09-23T00:00:00",
          "2021-09-24T00:00:00",
          "2021-09-27T00:00:00",
          "2021-09-28T00:00:00",
          "2021-09-29T00:00:00",
          "2021-09-30T00:00:00",
          "2021-10-01T00:00:00",
          "2021-10-04T00:00:00",
          "2021-10-05T00:00:00",
          "2021-10-06T00:00:00",
          "2021-10-07T00:00:00",
          "2021-10-08T00:00:00",
          "2021-10-11T00:00:00",
          "2021-10-12T00:00:00",
          "2021-10-13T00:00:00",
          "2021-10-14T00:00:00",
          "2021-10-15T00:00:00",
          "2021-10-18T00:00:00",
          "2021-10-19T00:00:00",
          "2021-10-20T00:00:00",
          "2021-10-21T00:00:00",
          "2021-10-22T00:00:00",
          "2021-10-25T00:00:00",
          "2021-10-26T00:00:00",
          "2021-10-27T00:00:00",
          "2021-10-28T00:00:00",
          "2021-10-29T00:00:00",
          "2021-11-01T00:00:00",
          "2021-11-02T00:00:00",
          "2021-11-03T00:00:00",
          "2021-11-04T00:00:00",
          "2021-11-05T00:00:00",
          "2021-11-08T00:00:00",
          "2021-11-09T00:00:00",
          "2021-11-10T00:00:00",
          "2021-11-11T00:00:00",
          "2021-11-12T00:00:00",
          "2021-11-15T00:00:00",
          "2021-11-16T00:00:00",
          "2021-11-17T00:00:00",
          "2021-11-18T00:00:00",
          "2021-11-19T00:00:00",
          "2021-11-22T00:00:00",
          "2021-11-23T00:00:00",
          "2021-11-24T00:00:00",
          "2021-11-26T00:00:00",
          "2021-11-29T00:00:00",
          "2021-11-30T00:00:00",
          "2021-12-01T00:00:00",
          "2021-12-02T00:00:00",
          "2021-12-03T00:00:00",
          "2021-12-06T00:00:00",
          "2021-12-07T00:00:00",
          "2021-12-08T00:00:00",
          "2021-12-09T00:00:00",
          "2021-12-10T00:00:00",
          "2021-12-13T00:00:00",
          "2021-12-14T00:00:00",
          "2021-12-15T00:00:00",
          "2021-12-16T00:00:00",
          "2021-12-17T00:00:00",
          "2021-12-20T00:00:00",
          "2021-12-21T00:00:00",
          "2021-12-22T00:00:00",
          "2021-12-23T00:00:00",
          "2021-12-27T00:00:00",
          "2021-12-28T00:00:00",
          "2021-12-29T00:00:00",
          "2021-12-30T00:00:00",
          "2021-12-31T00:00:00",
          "2022-01-03T00:00:00",
          "2022-01-04T00:00:00",
          "2022-01-05T00:00:00",
          "2022-01-06T00:00:00",
          "2022-01-07T00:00:00",
          "2022-01-10T00:00:00",
          "2022-01-11T00:00:00",
          "2022-01-12T00:00:00",
          "2022-01-13T00:00:00",
          "2022-01-14T00:00:00",
          "2022-01-18T00:00:00",
          "2022-01-19T00:00:00",
          "2022-01-20T00:00:00",
          "2022-01-21T00:00:00",
          "2022-01-24T00:00:00",
          "2022-01-25T00:00:00",
          "2022-01-26T00:00:00",
          "2022-01-27T00:00:00",
          "2022-01-28T00:00:00",
          "2022-01-31T00:00:00",
          "2022-02-01T00:00:00",
          "2022-02-02T00:00:00",
          "2022-02-03T00:00:00",
          "2022-02-04T00:00:00",
          "2022-02-07T00:00:00",
          "2022-02-08T00:00:00",
          "2022-02-09T00:00:00",
          "2022-02-10T00:00:00",
          "2022-02-11T00:00:00",
          "2022-02-14T00:00:00",
          "2022-02-15T00:00:00",
          "2022-02-16T00:00:00",
          "2022-02-17T00:00:00",
          "2022-02-18T00:00:00",
          "2022-02-22T00:00:00",
          "2022-02-23T00:00:00",
          "2022-02-24T00:00:00",
          "2022-02-25T00:00:00",
          "2022-02-28T00:00:00",
          "2022-03-01T00:00:00",
          "2022-03-02T00:00:00",
          "2022-03-03T00:00:00",
          "2022-03-04T00:00:00",
          "2022-03-07T00:00:00",
          "2022-03-08T00:00:00",
          "2022-03-09T00:00:00",
          "2022-03-10T00:00:00",
          "2022-03-11T00:00:00",
          "2022-03-14T00:00:00",
          "2022-03-15T00:00:00",
          "2022-03-16T00:00:00",
          "2022-03-17T00:00:00",
          "2022-03-18T00:00:00",
          "2022-03-21T00:00:00",
          "2022-03-22T00:00:00",
          "2022-03-23T00:00:00",
          "2022-03-24T00:00:00",
          "2022-03-25T00:00:00",
          "2022-03-28T00:00:00",
          "2022-03-29T00:00:00",
          "2022-03-30T00:00:00",
          "2022-03-31T00:00:00",
          "2022-04-01T00:00:00",
          "2022-04-04T00:00:00",
          "2022-04-05T00:00:00",
          "2022-04-06T00:00:00",
          "2022-04-07T00:00:00",
          "2022-04-08T00:00:00",
          "2022-04-11T00:00:00",
          "2022-04-12T00:00:00",
          "2022-04-13T00:00:00",
          "2022-04-14T00:00:00",
          "2022-04-18T00:00:00",
          "2022-04-19T00:00:00",
          "2022-04-20T00:00:00",
          "2022-04-21T00:00:00",
          "2022-04-22T00:00:00",
          "2022-04-25T00:00:00",
          "2022-04-26T00:00:00",
          "2022-04-27T00:00:00",
          "2022-04-28T00:00:00",
          "2022-04-29T00:00:00",
          "2022-05-02T00:00:00",
          "2022-05-03T00:00:00",
          "2022-05-04T00:00:00",
          "2022-05-05T00:00:00",
          "2022-05-06T00:00:00",
          "2022-05-09T00:00:00",
          "2022-05-10T00:00:00",
          "2022-05-11T00:00:00",
          "2022-05-12T00:00:00",
          "2022-05-13T00:00:00",
          "2022-05-16T00:00:00",
          "2022-05-17T00:00:00",
          "2022-05-18T00:00:00",
          "2022-05-19T00:00:00",
          "2022-05-20T00:00:00",
          "2022-05-23T00:00:00",
          "2022-05-24T00:00:00",
          "2022-05-25T00:00:00",
          "2022-05-26T00:00:00",
          "2022-05-27T00:00:00",
          "2022-05-31T00:00:00",
          "2022-06-01T00:00:00",
          "2022-06-02T00:00:00",
          "2022-06-03T00:00:00",
          "2022-06-06T00:00:00",
          "2022-06-07T00:00:00",
          "2022-06-08T00:00:00",
          "2022-06-09T00:00:00",
          "2022-06-10T00:00:00",
          "2022-06-13T00:00:00",
          "2022-06-14T00:00:00",
          "2022-06-15T00:00:00",
          "2022-06-16T00:00:00",
          "2022-06-17T00:00:00",
          "2022-06-21T00:00:00",
          "2022-06-22T00:00:00",
          "2022-06-23T00:00:00",
          "2022-06-24T00:00:00",
          "2022-06-27T00:00:00",
          "2022-06-28T00:00:00",
          "2022-06-29T00:00:00",
          "2022-06-30T00:00:00",
          "2022-07-01T00:00:00",
          "2022-07-05T00:00:00",
          "2022-07-06T00:00:00",
          "2022-07-07T00:00:00",
          "2022-07-08T00:00:00",
          "2022-07-11T00:00:00",
          "2022-07-12T00:00:00",
          "2022-07-13T00:00:00",
          "2022-07-14T00:00:00",
          "2022-07-15T00:00:00",
          "2022-07-18T00:00:00",
          "2022-07-19T00:00:00",
          "2022-07-20T00:00:00",
          "2022-07-21T00:00:00",
          "2022-07-22T00:00:00",
          "2022-07-25T00:00:00",
          "2022-07-26T00:00:00",
          "2022-07-27T00:00:00",
          "2022-07-28T00:00:00",
          "2022-07-29T00:00:00",
          "2022-08-01T00:00:00",
          "2022-08-02T00:00:00",
          "2022-08-03T00:00:00",
          "2022-08-04T00:00:00",
          "2022-08-05T00:00:00",
          "2022-08-08T00:00:00",
          "2022-08-09T00:00:00",
          "2022-08-10T00:00:00",
          "2022-08-11T00:00:00",
          "2022-08-12T00:00:00",
          "2022-08-15T00:00:00",
          "2022-08-16T00:00:00",
          "2022-08-17T00:00:00",
          "2022-08-18T00:00:00",
          "2022-08-19T00:00:00",
          "2022-08-22T00:00:00",
          "2022-08-23T00:00:00",
          "2022-08-24T00:00:00",
          "2022-08-25T00:00:00",
          "2022-08-26T00:00:00",
          "2022-08-29T00:00:00",
          "2022-08-30T00:00:00",
          "2022-08-31T00:00:00",
          "2022-09-01T00:00:00",
          "2022-09-02T00:00:00",
          "2022-09-06T00:00:00",
          "2022-09-07T00:00:00",
          "2022-09-08T00:00:00",
          "2022-09-09T00:00:00",
          "2022-09-12T00:00:00",
          "2022-09-13T00:00:00",
          "2022-09-14T00:00:00",
          "2022-09-15T00:00:00",
          "2022-09-16T00:00:00",
          "2022-09-19T00:00:00",
          "2022-09-20T00:00:00",
          "2022-09-21T00:00:00",
          "2022-09-22T00:00:00",
          "2022-09-23T00:00:00",
          "2022-09-26T00:00:00",
          "2022-09-27T00:00:00",
          "2022-09-28T00:00:00",
          "2022-09-29T00:00:00",
          "2022-09-30T00:00:00",
          "2022-10-03T00:00:00",
          "2022-10-04T00:00:00",
          "2022-10-05T00:00:00",
          "2022-10-06T00:00:00",
          "2022-10-07T00:00:00",
          "2022-10-10T00:00:00",
          "2022-10-11T00:00:00",
          "2022-10-12T00:00:00",
          "2022-10-13T00:00:00",
          "2022-10-14T00:00:00",
          "2022-10-17T00:00:00",
          "2022-10-18T00:00:00",
          "2022-10-19T00:00:00",
          "2022-10-20T00:00:00",
          "2022-10-21T00:00:00",
          "2022-10-24T00:00:00",
          "2022-10-25T00:00:00",
          "2022-10-26T00:00:00",
          "2022-10-27T00:00:00",
          "2022-10-28T00:00:00",
          "2022-10-31T00:00:00",
          "2022-11-01T00:00:00",
          "2022-11-02T00:00:00",
          "2022-11-03T00:00:00",
          "2022-11-04T00:00:00",
          "2022-11-07T00:00:00",
          "2022-11-08T00:00:00",
          "2022-11-09T00:00:00",
          "2022-11-10T00:00:00",
          "2022-11-11T00:00:00",
          "2022-11-14T00:00:00",
          "2022-11-15T00:00:00",
          "2022-11-16T00:00:00",
          "2022-11-17T00:00:00",
          "2022-11-18T00:00:00",
          "2022-11-21T00:00:00",
          "2022-11-22T00:00:00",
          "2022-11-23T00:00:00",
          "2022-11-25T00:00:00",
          "2022-11-28T00:00:00",
          "2022-11-29T00:00:00",
          "2022-11-30T00:00:00",
          "2022-12-01T00:00:00",
          "2022-12-02T00:00:00",
          "2022-12-05T00:00:00",
          "2022-12-06T00:00:00",
          "2022-12-07T00:00:00",
          "2022-12-08T00:00:00",
          "2022-12-09T00:00:00",
          "2022-12-12T00:00:00",
          "2022-12-13T00:00:00",
          "2022-12-14T00:00:00",
          "2022-12-15T00:00:00",
          "2022-12-16T00:00:00",
          "2022-12-19T00:00:00",
          "2022-12-20T00:00:00",
          "2022-12-21T00:00:00",
          "2022-12-22T00:00:00",
          "2022-12-23T00:00:00",
          "2022-12-27T00:00:00",
          "2022-12-28T00:00:00",
          "2022-12-29T00:00:00",
          "2022-12-30T00:00:00",
          "2023-01-03T00:00:00",
          "2023-01-04T00:00:00",
          "2023-01-05T00:00:00",
          "2023-01-06T00:00:00",
          "2023-01-09T00:00:00",
          "2023-01-10T00:00:00",
          "2023-01-11T00:00:00",
          "2023-01-12T00:00:00",
          "2023-01-13T00:00:00",
          "2023-01-17T00:00:00",
          "2023-01-18T00:00:00",
          "2023-01-19T00:00:00",
          "2023-01-20T00:00:00",
          "2023-01-23T00:00:00",
          "2023-01-24T00:00:00",
          "2023-01-25T00:00:00",
          "2023-01-26T00:00:00",
          "2023-01-27T00:00:00",
          "2023-01-30T00:00:00",
          "2023-01-31T00:00:00",
          "2023-02-01T00:00:00",
          "2023-02-02T00:00:00",
          "2023-02-03T00:00:00",
          "2023-02-06T00:00:00",
          "2023-02-07T00:00:00",
          "2023-02-08T00:00:00",
          "2023-02-09T00:00:00",
          "2023-02-10T00:00:00",
          "2023-02-13T00:00:00",
          "2023-02-14T00:00:00",
          "2023-02-15T00:00:00",
          "2023-02-16T00:00:00",
          "2023-02-17T00:00:00",
          "2023-02-21T00:00:00",
          "2023-02-22T00:00:00",
          "2023-02-23T00:00:00",
          "2023-02-24T00:00:00",
          "2023-02-27T00:00:00",
          "2023-02-28T00:00:00",
          "2023-03-01T00:00:00",
          "2023-03-02T00:00:00",
          "2023-03-03T00:00:00",
          "2023-03-06T00:00:00",
          "2023-03-07T00:00:00",
          "2023-03-08T00:00:00",
          "2023-03-09T00:00:00",
          "2023-03-10T00:00:00",
          "2023-03-13T00:00:00",
          "2023-03-14T00:00:00",
          "2023-03-15T00:00:00",
          "2023-03-16T00:00:00",
          "2023-03-17T00:00:00",
          "2023-03-20T00:00:00",
          "2023-03-21T00:00:00",
          "2023-03-22T00:00:00",
          "2023-03-23T00:00:00",
          "2023-03-24T00:00:00",
          "2023-03-27T00:00:00",
          "2023-03-28T00:00:00",
          "2023-03-29T00:00:00",
          "2023-03-30T00:00:00",
          "2023-03-31T00:00:00",
          "2023-04-03T00:00:00",
          "2023-04-04T00:00:00",
          "2023-04-05T00:00:00",
          "2023-04-06T00:00:00",
          "2023-04-10T00:00:00",
          "2023-04-11T00:00:00",
          "2023-04-12T00:00:00",
          "2023-04-13T00:00:00",
          "2023-04-14T00:00:00",
          "2023-04-17T00:00:00",
          "2023-04-18T00:00:00",
          "2023-04-19T00:00:00",
          "2023-04-20T00:00:00",
          "2023-04-21T00:00:00",
          "2023-04-24T00:00:00",
          "2023-04-25T00:00:00",
          "2023-04-26T00:00:00",
          "2023-04-27T00:00:00",
          "2023-04-28T00:00:00",
          "2023-05-01T00:00:00",
          "2023-05-02T00:00:00",
          "2023-05-03T00:00:00",
          "2023-05-04T00:00:00",
          "2023-05-05T00:00:00",
          "2023-05-08T00:00:00",
          "2023-05-09T00:00:00",
          "2023-05-10T00:00:00",
          "2023-05-11T00:00:00",
          "2023-05-12T00:00:00",
          "2023-05-15T00:00:00",
          "2023-05-16T00:00:00",
          "2023-05-17T00:00:00",
          "2023-05-18T00:00:00",
          "2023-05-19T00:00:00",
          "2023-05-22T00:00:00",
          "2023-05-23T00:00:00",
          "2023-05-24T00:00:00",
          "2023-05-25T00:00:00",
          "2023-05-26T00:00:00",
          "2023-05-30T00:00:00",
          "2023-05-31T00:00:00",
          "2023-06-01T00:00:00",
          "2023-06-02T00:00:00",
          "2023-06-05T00:00:00",
          "2023-06-06T00:00:00",
          "2023-06-07T00:00:00",
          "2023-06-08T00:00:00",
          "2023-06-09T00:00:00",
          "2023-06-12T00:00:00",
          "2023-06-13T00:00:00",
          "2023-06-14T00:00:00",
          "2023-06-15T00:00:00",
          "2023-06-16T00:00:00",
          "2023-06-20T00:00:00",
          "2023-06-21T00:00:00",
          "2023-06-22T00:00:00",
          "2023-06-23T00:00:00",
          "2023-06-26T00:00:00",
          "2023-06-27T00:00:00",
          "2023-06-28T00:00:00",
          "2023-06-29T00:00:00",
          "2023-06-30T00:00:00",
          "2023-07-03T00:00:00",
          "2023-07-05T00:00:00",
          "2023-07-06T00:00:00",
          "2023-07-07T00:00:00",
          "2023-07-10T00:00:00",
          "2023-07-11T00:00:00",
          "2023-07-12T00:00:00",
          "2023-07-13T00:00:00",
          "2023-07-14T00:00:00",
          "2023-07-17T00:00:00",
          "2023-07-18T00:00:00",
          "2023-07-19T00:00:00",
          "2023-07-20T00:00:00",
          "2023-07-21T00:00:00",
          "2023-07-24T00:00:00",
          "2023-07-25T00:00:00",
          "2023-07-26T00:00:00",
          "2023-07-27T00:00:00",
          "2023-07-28T00:00:00",
          "2023-07-31T00:00:00",
          "2023-08-01T00:00:00",
          "2023-08-02T00:00:00",
          "2023-08-03T00:00:00",
          "2023-08-04T00:00:00",
          "2023-08-07T00:00:00",
          "2023-08-08T00:00:00",
          "2023-08-09T00:00:00",
          "2023-08-10T00:00:00",
          "2023-08-11T00:00:00",
          "2023-08-14T00:00:00",
          "2023-08-15T00:00:00",
          "2023-08-16T00:00:00",
          "2023-08-17T00:00:00",
          "2023-08-18T00:00:00",
          "2023-08-21T00:00:00",
          "2023-08-22T00:00:00",
          "2023-08-23T00:00:00",
          "2023-08-24T00:00:00",
          "2023-08-25T00:00:00",
          "2023-08-28T00:00:00",
          "2023-08-29T00:00:00",
          "2023-08-30T00:00:00",
          "2023-08-31T00:00:00",
          "2023-09-01T00:00:00",
          "2023-09-05T00:00:00",
          "2023-09-06T00:00:00",
          "2023-09-07T00:00:00",
          "2023-09-08T00:00:00",
          "2023-09-11T00:00:00",
          "2023-09-12T00:00:00",
          "2023-09-13T00:00:00",
          "2023-09-14T00:00:00",
          "2023-09-15T00:00:00",
          "2023-09-18T00:00:00",
          "2023-09-19T00:00:00",
          "2023-09-20T00:00:00",
          "2023-09-21T00:00:00",
          "2023-09-22T00:00:00",
          "2023-09-25T00:00:00",
          "2023-09-26T00:00:00",
          "2023-09-27T00:00:00",
          "2023-09-28T00:00:00",
          "2023-09-29T00:00:00",
          "2023-10-02T00:00:00",
          "2023-10-03T00:00:00",
          "2023-10-04T00:00:00",
          "2023-10-05T00:00:00",
          "2023-10-06T00:00:00",
          "2023-10-09T00:00:00",
          "2023-10-10T00:00:00",
          "2023-10-11T00:00:00",
          "2023-10-12T00:00:00",
          "2023-10-13T00:00:00",
          "2023-10-16T00:00:00",
          "2023-10-17T00:00:00",
          "2023-10-18T00:00:00",
          "2023-10-19T00:00:00",
          "2023-10-20T00:00:00",
          "2023-10-23T00:00:00",
          "2023-10-24T00:00:00",
          "2023-10-25T00:00:00",
          "2023-10-26T00:00:00",
          "2023-10-27T00:00:00",
          "2023-10-30T00:00:00",
          "2023-10-31T00:00:00",
          "2023-11-01T00:00:00",
          "2023-11-02T00:00:00",
          "2023-11-03T00:00:00",
          "2023-11-06T00:00:00",
          "2023-11-07T00:00:00",
          "2023-11-08T00:00:00",
          "2023-11-09T00:00:00",
          "2023-11-10T00:00:00",
          "2023-11-13T00:00:00",
          "2023-11-14T00:00:00",
          "2023-11-15T00:00:00",
          "2023-11-16T00:00:00",
          "2023-11-17T00:00:00",
          "2023-11-20T00:00:00",
          "2023-11-21T00:00:00",
          "2023-11-22T00:00:00",
          "2023-11-24T00:00:00",
          "2023-11-27T00:00:00",
          "2023-11-28T00:00:00",
          "2023-11-29T00:00:00",
          "2023-11-30T00:00:00",
          "2023-12-01T00:00:00",
          "2023-12-04T00:00:00",
          "2023-12-05T00:00:00",
          "2023-12-06T00:00:00",
          "2023-12-07T00:00:00",
          "2023-12-08T00:00:00",
          "2023-12-11T00:00:00",
          "2023-12-12T00:00:00",
          "2023-12-13T00:00:00",
          "2023-12-14T00:00:00",
          "2023-12-15T00:00:00",
          "2023-12-18T00:00:00",
          "2023-12-19T00:00:00",
          "2023-12-20T00:00:00",
          "2023-12-21T00:00:00",
          "2023-12-22T00:00:00",
          "2023-12-26T00:00:00",
          "2023-12-27T00:00:00",
          "2023-12-28T00:00:00",
          "2023-12-29T00:00:00",
          "2024-01-02T00:00:00",
          "2024-01-03T00:00:00",
          "2024-01-04T00:00:00",
          "2024-01-05T00:00:00",
          "2024-01-08T00:00:00",
          "2024-01-09T00:00:00",
          "2024-01-10T00:00:00",
          "2024-01-11T00:00:00",
          "2024-01-12T00:00:00",
          "2024-01-16T00:00:00",
          "2024-01-17T00:00:00",
          "2024-01-18T00:00:00",
          "2024-01-19T00:00:00",
          "2024-01-22T00:00:00",
          "2024-01-23T00:00:00",
          "2024-01-24T00:00:00",
          "2024-01-25T00:00:00",
          "2024-01-26T00:00:00",
          "2024-01-29T00:00:00",
          "2024-01-30T00:00:00",
          "2024-01-31T00:00:00",
          "2024-02-01T00:00:00",
          "2024-02-02T00:00:00",
          "2024-02-05T00:00:00",
          "2024-02-06T00:00:00",
          "2024-02-07T00:00:00",
          "2024-02-08T00:00:00",
          "2024-02-09T00:00:00",
          "2024-02-12T00:00:00",
          "2024-02-13T00:00:00",
          "2024-02-14T00:00:00",
          "2024-02-15T00:00:00",
          "2024-02-16T00:00:00",
          "2024-02-20T00:00:00",
          "2024-02-21T00:00:00",
          "2024-02-22T00:00:00",
          "2024-02-23T00:00:00",
          "2024-02-26T00:00:00",
          "2024-02-27T00:00:00",
          "2024-02-28T00:00:00",
          "2024-02-29T00:00:00",
          "2024-03-01T00:00:00",
          "2024-03-04T00:00:00",
          "2024-03-05T00:00:00",
          "2024-03-06T00:00:00",
          "2024-03-07T00:00:00",
          "2024-03-08T00:00:00",
          "2024-03-11T00:00:00",
          "2024-03-12T00:00:00",
          "2024-03-13T00:00:00",
          "2024-03-14T00:00:00",
          "2024-03-15T00:00:00",
          "2024-03-18T00:00:00",
          "2024-03-19T00:00:00",
          "2024-03-20T00:00:00",
          "2024-03-21T00:00:00",
          "2024-03-22T00:00:00",
          "2024-03-25T00:00:00",
          "2024-03-26T00:00:00",
          "2024-03-27T00:00:00",
          "2024-03-28T00:00:00",
          "2024-04-01T00:00:00",
          "2024-04-02T00:00:00",
          "2024-04-03T00:00:00",
          "2024-04-04T00:00:00",
          "2024-04-05T00:00:00",
          "2024-04-08T00:00:00",
          "2024-04-09T00:00:00",
          "2024-04-10T00:00:00",
          "2024-04-11T00:00:00",
          "2024-04-12T00:00:00",
          "2024-04-15T00:00:00",
          "2024-04-16T00:00:00",
          "2024-04-17T00:00:00",
          "2024-04-18T00:00:00",
          "2024-04-19T00:00:00",
          "2024-04-22T00:00:00",
          "2024-04-23T00:00:00",
          "2024-04-24T00:00:00",
          "2024-04-25T00:00:00",
          "2024-04-26T00:00:00",
          "2024-04-29T00:00:00",
          "2024-04-30T00:00:00",
          "2024-05-01T00:00:00",
          "2024-05-02T00:00:00",
          "2024-05-03T00:00:00",
          "2024-05-06T00:00:00",
          "2024-05-07T00:00:00",
          "2024-05-08T00:00:00",
          "2024-05-09T00:00:00",
          "2024-05-10T00:00:00",
          "2024-05-13T00:00:00",
          "2024-05-14T00:00:00",
          "2024-05-15T00:00:00",
          "2024-05-16T00:00:00",
          "2024-05-17T00:00:00",
          "2024-05-20T00:00:00",
          "2024-05-21T00:00:00",
          "2024-05-22T00:00:00",
          "2024-05-23T00:00:00",
          "2024-05-24T00:00:00",
          "2024-05-28T00:00:00",
          "2024-05-29T00:00:00",
          "2024-05-30T00:00:00",
          "2024-05-31T00:00:00",
          "2024-06-03T00:00:00",
          "2024-06-04T00:00:00",
          "2024-06-05T00:00:00",
          "2024-06-06T00:00:00",
          "2024-06-07T00:00:00",
          "2024-06-10T00:00:00",
          "2024-06-11T00:00:00",
          "2024-06-12T00:00:00",
          "2024-06-13T00:00:00",
          "2024-06-14T00:00:00",
          "2024-06-17T00:00:00",
          "2024-06-18T00:00:00",
          "2024-06-20T00:00:00",
          "2024-06-21T00:00:00",
          "2024-06-24T00:00:00",
          "2024-06-25T00:00:00",
          "2024-06-26T00:00:00",
          "2024-06-27T00:00:00",
          "2024-06-28T00:00:00",
          "2024-07-01T00:00:00",
          "2024-07-02T00:00:00",
          "2024-07-03T00:00:00",
          "2024-07-05T00:00:00",
          "2024-07-08T00:00:00",
          "2024-07-09T00:00:00",
          "2024-07-10T00:00:00",
          "2024-07-11T00:00:00",
          "2024-07-12T00:00:00",
          "2024-07-15T00:00:00",
          "2024-07-16T00:00:00",
          "2024-07-17T00:00:00",
          "2024-07-18T00:00:00",
          "2024-07-19T00:00:00",
          "2024-07-22T00:00:00",
          "2024-07-23T00:00:00",
          "2024-07-24T00:00:00",
          "2024-07-25T00:00:00",
          "2024-07-26T00:00:00",
          "2024-07-29T00:00:00",
          "2024-07-30T00:00:00",
          "2024-07-31T00:00:00",
          "2024-08-01T00:00:00",
          "2024-08-02T00:00:00",
          "2024-08-05T00:00:00",
          "2024-08-06T00:00:00",
          "2024-08-07T00:00:00",
          "2024-08-08T00:00:00",
          "2024-08-09T00:00:00",
          "2024-08-12T00:00:00",
          "2024-08-13T00:00:00",
          "2024-08-14T00:00:00",
          "2024-08-15T00:00:00",
          "2024-08-16T00:00:00",
          "2024-08-19T00:00:00",
          "2024-08-20T00:00:00",
          "2024-08-21T00:00:00",
          "2024-08-22T00:00:00",
          "2024-08-23T00:00:00",
          "2024-08-26T00:00:00",
          "2024-08-27T00:00:00",
          "2024-08-28T00:00:00",
          "2024-08-29T00:00:00",
          "2024-08-30T00:00:00",
          "2024-09-03T00:00:00",
          "2024-09-04T00:00:00",
          "2024-09-05T00:00:00",
          "2024-09-06T00:00:00",
          "2024-09-09T00:00:00",
          "2024-09-10T00:00:00",
          "2024-09-11T00:00:00",
          "2024-09-12T00:00:00",
          "2024-09-13T00:00:00",
          "2024-09-16T00:00:00",
          "2024-09-17T00:00:00",
          "2024-09-18T00:00:00",
          "2024-09-19T00:00:00",
          "2024-09-20T00:00:00",
          "2024-09-23T00:00:00",
          "2024-09-24T00:00:00",
          "2024-09-25T00:00:00",
          "2024-09-26T00:00:00",
          "2024-09-27T00:00:00",
          "2024-09-30T00:00:00",
          "2024-10-01T00:00:00",
          "2024-10-02T00:00:00",
          "2024-10-03T00:00:00",
          "2024-10-04T00:00:00",
          "2024-10-07T00:00:00",
          "2024-10-08T00:00:00",
          "2024-10-09T00:00:00",
          "2024-10-10T00:00:00",
          "2024-10-11T00:00:00",
          "2024-10-14T00:00:00",
          "2024-10-15T00:00:00",
          "2024-10-16T00:00:00",
          "2024-10-17T00:00:00",
          "2024-10-18T00:00:00",
          "2024-10-21T00:00:00",
          "2024-10-22T00:00:00",
          "2024-10-23T00:00:00",
          "2024-10-24T00:00:00",
          "2024-10-25T00:00:00",
          "2024-10-28T00:00:00",
          "2024-10-29T00:00:00",
          "2024-10-30T00:00:00",
          "2024-10-31T00:00:00",
          "2024-11-01T00:00:00",
          "2024-11-04T00:00:00",
          "2024-11-05T00:00:00",
          "2024-11-06T00:00:00",
          "2024-11-07T00:00:00",
          "2024-11-08T00:00:00",
          "2024-11-11T00:00:00",
          "2024-11-12T00:00:00",
          "2024-11-13T00:00:00",
          "2024-11-14T00:00:00",
          "2024-11-15T00:00:00",
          "2024-11-18T00:00:00",
          "2024-11-19T00:00:00",
          "2024-11-20T00:00:00",
          "2024-11-21T00:00:00",
          "2024-11-22T00:00:00",
          "2024-11-25T00:00:00",
          "2024-11-26T00:00:00",
          "2024-11-27T00:00:00",
          "2024-11-29T00:00:00",
          "2024-12-02T00:00:00",
          "2024-12-03T00:00:00",
          "2024-12-04T00:00:00",
          "2024-12-05T00:00:00",
          "2024-12-06T00:00:00",
          "2024-12-09T00:00:00",
          "2024-12-10T00:00:00",
          "2024-12-11T00:00:00",
          "2024-12-12T00:00:00",
          "2024-12-13T00:00:00",
          "2024-12-16T00:00:00",
          "2024-12-17T00:00:00",
          "2024-12-18T00:00:00",
          "2024-12-19T00:00:00",
          "2024-12-20T00:00:00",
          "2024-12-23T00:00:00",
          "2024-12-24T00:00:00",
          "2024-12-26T00:00:00",
          "2024-12-27T00:00:00",
          "2024-12-30T00:00:00"
         ],
         "y": [
          [
           24.347169876098633
          ],
          [
           23.661270141601562
          ],
          [
           23.66349983215332
          ],
          [
           23.995311737060547
          ],
          [
           24.91727066040039
          ],
          [
           24.943984985351562
          ],
          [
           24.329345703125
          ],
          [
           24.545366287231445
          ],
          [
           24.45183563232422
          ],
          [
           23.788209915161133
          ],
          [
           23.603368759155273
          ],
          [
           24.211326599121094
          ],
          [
           24.396163940429688
          ],
          [
           25.030839920043945
          ],
          [
           25.160005569458008
          ],
          [
           25.186721801757812
          ],
          [
           24.30485725402832
          ],
          [
           25.678884506225586
          ],
          [
           26.47835922241211
          ],
          [
           26.09087371826172
          ],
          [
           26.418222427368164
          ],
          [
           26.422679901123047
          ],
          [
           26.625335693359375
          ],
          [
           26.81537628173828
          ],
          [
           26.58955955505371
          ],
          [
           26.766185760498047
          ],
          [
           27.280405044555664
          ],
          [
           27.919824600219727
          ],
          [
           28.273069381713867
          ],
          [
           28.411684036254883
          ],
          [
           28.579370498657227
          ],
          [
           28.778348922729492
          ],
          [
           28.717979431152344
          ],
          [
           28.952733993530273
          ],
          [
           29.735244750976562
          ],
          [
           29.54967498779297
          ],
          [
           28.793991088867188
          ],
          [
           29.158418655395508
          ],
          [
           28.720216751098633
          ],
          [
           28.86107063293457
          ],
          [
           28.92142677307129
          ],
          [
           28.738096237182617
          ],
          [
           28.26189422607422
          ],
          [
           28.304370880126953
          ],
          [
           28.425092697143555
          ],
          [
           27.837100982666016
          ],
          [
           27.32958984375
          ],
          [
           27.823688507080078
          ],
          [
           27.63141632080078
          ],
          [
           27.93547248840332
          ],
          [
           28.40274429321289
          ],
          [
           28.722454071044922
          ],
          [
           28.505586624145508
          ],
          [
           28.14787483215332
          ],
          [
           28.440752029418945
          ],
          [
           28.32448959350586
          ],
          [
           27.58446502685547
          ],
          [
           27.776742935180664
          ],
          [
           27.555400848388672
          ],
          [
           28.252944946289062
          ],
          [
           27.819211959838867
          ],
          [
           27.778972625732422
          ],
          [
           28.018203735351562
          ],
          [
           28.472049713134766
          ],
          [
           28.172468185424805
          ],
          [
           28.080799102783203
          ],
          [
           28.29542350769043
          ],
          [
           28.416160583496094
          ],
          [
           28.360261917114258
          ],
          [
           28.23729133605957
          ],
          [
           28.34461212158203
          ],
          [
           28.208227157592773
          ],
          [
           27.890758514404297
          ],
          [
           28.527944564819336
          ],
          [
           28.373680114746094
          ],
          [
           28.755998611450195
          ],
          [
           28.990747451782227
          ],
          [
           29.12711524963379
          ],
          [
           29.656993865966797
          ],
          [
           29.189722061157227
          ],
          [
           28.760454177856445
          ],
          [
           27.980188369750977
          ],
          [
           28.82977294921875
          ],
          [
           28.77387809753418
          ],
          [
           28.125516891479492
          ],
          [
           27.948890686035156
          ],
          [
           28.12175750732422
          ],
          [
           28.651596069335938
          ],
          [
           28.3597354888916
          ],
          [
           28.258712768554688
          ],
          [
           28.290145874023438
          ],
          [
           28.950197219848633
          ],
          [
           28.909778594970703
          ],
          [
           29.22858238220215
          ],
          [
           29.20163917541504
          ],
          [
           29.199392318725586
          ],
          [
           29.497989654541016
          ],
          [
           29.75617218017578
          ],
          [
           29.100608825683594
          ],
          [
           29.64391326904297
          ],
          [
           29.585542678833008
          ],
          [
           29.248781204223633
          ],
          [
           29.307151794433594
          ],
          [
           29.17693519592285
          ],
          [
           29.212862014770508
          ],
          [
           29.042232513427734
          ],
          [
           28.882835388183594
          ],
          [
           28.692007064819336
          ],
          [
           28.606689453125
          ],
          [
           28.93447494506836
          ],
          [
           28.869367599487305
          ],
          [
           28.550567626953125
          ],
          [
           28.494436264038086
          ],
          [
           28.64710807800293
          ],
          [
           28.57975196838379
          ],
          [
           28.70996856689453
          ],
          [
           28.42259979248047
          ],
          [
           28.64934730529785
          ],
          [
           28.519134521484375
          ],
          [
           28.761600494384766
          ],
          [
           28.624656677246094
          ],
          [
           28.456274032592773
          ],
          [
           27.957870483398438
          ],
          [
           28.159931182861328
          ],
          [
           28.42259979248047
          ],
          [
           28.386682510375977
          ],
          [
           28.28788948059082
          ],
          [
           28.218299865722656
          ],
          [
           27.51783561706543
          ],
          [
           26.956565856933594
          ],
          [
           27.677236557006836
          ],
          [
           28.211563110351562
          ],
          [
           28.200334548950195
          ],
          [
           28.471996307373047
          ],
          [
           28.85140037536621
          ],
          [
           29.100608825683594
          ],
          [
           29.650653839111328
          ],
          [
           29.35430145263672
          ],
          [
           28.112777709960938
          ],
          [
           28.099306106567383
          ],
          [
           27.95113754272461
          ],
          [
           27.562725067138672
          ],
          [
           27.699687957763672
          ],
          [
           27.61212921142578
          ],
          [
           27.47293472290039
          ],
          [
           27.232711791992188
          ],
          [
           26.59061622619629
          ],
          [
           25.73749351501465
          ],
          [
           25.908119201660156
          ],
          [
           25.96449851989746
          ],
          [
           26.052457809448242
          ],
          [
           26.999652862548828
          ],
          [
           25.59464454650879
          ],
          [
           25.989299774169922
          ],
          [
           25.969009399414062
          ],
          [
           26.151681900024414
          ],
          [
           26.42231559753418
          ],
          [
           26.27347183227539
          ],
          [
           25.93744468688965
          ],
          [
           25.405202865600586
          ],
          [
           23.85134506225586
          ],
          [
           23.255970001220703
          ],
          [
           23.395784378051758
          ],
          [
           24.737659454345703
          ],
          [
           25.46609115600586
          ],
          [
           25.54953956604004
          ],
          [
           25.43001937866211
          ],
          [
           24.29337501525879
          ],
          [
           25.335285186767578
          ],
          [
           24.89100456237793
          ],
          [
           24.642932891845703
          ],
          [
           25.328521728515625
          ],
          [
           24.841388702392578
          ],
          [
           25.38715934753418
          ],
          [
           25.757020950317383
          ],
          [
           26.00509262084961
          ],
          [
           26.22385025024414
          ],
          [
           26.25316619873047
          ],
          [
           25.691619873046875
          ],
          [
           25.585620880126953
          ],
          [
           25.982545852661133
          ],
          [
           25.574352264404297
          ],
          [
           25.781824111938477
          ],
          [
           25.935178756713867
          ],
          [
           25.869779586791992
          ],
          [
           25.357847213745117
          ],
          [
           24.595571517944336
          ],
          [
           24.875225067138672
          ],
          [
           24.71285057067871
          ],
          [
           24.893259048461914
          ],
          [
           24.983474731445312
          ],
          [
           25.10300064086914
          ],
          [
           24.983474731445312
          ],
          [
           24.694801330566406
          ],
          [
           25.28567886352539
          ],
          [
           25.16840171813965
          ],
          [
           25.21125602722168
          ],
          [
           24.85492706298828
          ],
          [
           25.227033615112305
          ],
          [
           25.042110443115234
          ],
          [
           25.197725296020508
          ],
          [
           25.657787322998047
          ],
          [
           25.655534744262695
          ],
          [
           26.047943115234375
          ],
          [
           26.855321884155273
          ],
          [
           25.998334884643555
          ],
          [
           25.83369255065918
          ],
          [
           26.89815902709961
          ],
          [
           27.18232536315918
          ],
          [
           26.950035095214844
          ],
          [
           27.32891273498535
          ],
          [
           27.642393112182617
          ],
          [
           27.51384735107422
          ],
          [
           27.387012481689453
          ],
          [
           27.418718338012695
          ],
          [
           27.3077392578125
          ],
          [
           26.447080612182617
          ],
          [
           26.2976016998291
          ],
          [
           26.209274291992188
          ],
          [
           25.443744659423828
          ],
          [
           25.86048126220703
          ],
          [
           25.749502182006836
          ],
          [
           26.56485366821289
          ],
          [
           26.902320861816406
          ],
          [
           27.020103454589844
          ],
          [
           26.66904067993164
          ],
          [
           26.92497444152832
          ],
          [
           26.732458114624023
          ],
          [
           26.68262481689453
          ],
          [
           26.793611526489258
          ],
          [
           26.576171875
          ],
          [
           26.33609962463379
          ],
          [
           26.091489791870117
          ],
          [
           26.95894432067871
          ],
          [
           26.789081573486328
          ],
          [
           26.777751922607422
          ],
          [
           26.186614990234375
          ],
          [
           26.311187744140625
          ],
          [
           25.633989334106445
          ],
          [
           25.475446701049805
          ],
          [
           25.024736404418945
          ],
          [
           25.217248916625977
          ],
          [
           24.6827335357666
          ],
          [
           24.01459312438965
          ],
          [
           24.309030532836914
          ],
          [
           24.286380767822266
          ],
          [
           24.59894561767578
          ],
          [
           24.467573165893555
          ],
          [
           24.193511962890625
          ],
          [
           24.628379821777344
          ],
          [
           24.306766510009766
          ],
          [
           23.840194702148438
          ],
          [
           23.860584259033203
          ],
          [
           23.262649536132812
          ],
          [
           22.80740737915039
          ],
          [
           21.844837188720703
          ],
          [
           21.960346221923828
          ],
          [
           22.31593132019043
          ],
          [
           22.639808654785156
          ],
          [
           22.057729721069336
          ],
          [
           22.5401554107666
          ],
          [
           21.998842239379883
          ],
          [
           21.89240074157715
          ],
          [
           21.921838760375977
          ],
          [
           21.81085968017578
          ],
          [
           22.970478057861328
          ],
          [
           22.522029876708984
          ],
          [
           22.646602630615234
          ],
          [
           21.1585693359375
          ],
          [
           21.310317993164062
          ],
          [
           22.046405792236328
          ],
          [
           21.84029769897461
          ],
          [
           21.39864730834961
          ],
          [
           21.822181701660156
          ],
          [
           21.997522354125977
          ],
          [
           21.410011291503906
          ],
          [
           21.635452270507812
          ],
          [
           21.630903244018555
          ],
          [
           21.46694564819336
          ],
          [
           21.337146759033203
          ],
          [
           21.403186798095703
          ],
          [
           22.006637573242188
          ],
          [
           22.343658447265625
          ],
          [
           21.92009925842285
          ],
          [
           21.870006561279297
          ],
          [
           22.061283111572266
          ],
          [
           21.56258773803711
          ],
          [
           21.883665084838867
          ],
          [
           22.03396224975586
          ],
          [
           22.0681209564209
          ],
          [
           22.018014907836914
          ],
          [
           22.8924617767334
          ],
          [
           22.942556381225586
          ],
          [
           23.11334228515625
          ],
          [
           23.457197189331055
          ],
          [
           23.19759750366211
          ],
          [
           23.006311416625977
          ],
          [
           23.026809692382812
          ],
          [
           23.038192749023438
          ],
          [
           23.286409378051758
          ],
          [
           23.345613479614258
          ],
          [
           23.814712524414062
          ],
          [
           24.13123893737793
          ],
          [
           24.092527389526367
          ],
          [
           24.119855880737305
          ],
          [
           24.117578506469727
          ],
          [
           24.302032470703125
          ],
          [
           24.16767120361328
          ],
          [
           24.062923431396484
          ],
          [
           23.95362091064453
          ],
          [
           24.52063751220703
          ],
          [
           24.948745727539062
          ],
          [
           24.818944931030273
          ],
          [
           25.04666519165039
          ],
          [
           25.303991317749023
          ],
          [
           25.005680084228516
          ],
          [
           25.26755714416504
          ],
          [
           24.716472625732422
          ],
          [
           24.743797302246094
          ],
          [
           24.82577896118164
          ],
          [
           25.149145126342773
          ],
          [
           25.513486862182617
          ],
          [
           25.527149200439453
          ],
          [
           25.014785766601562
          ],
          [
           24.47509765625
          ],
          [
           24.34529685974121
          ],
          [
           24.39539337158203
          ],
          [
           24.13123893737793
          ],
          [
           24.065200805664062
          ],
          [
           23.928577423095703
          ],
          [
           23.76234245300293
          ],
          [
           22.275341033935547
          ],
          [
           21.594465255737305
          ],
          [
           21.346254348754883
          ],
          [
           21.323484420776367
          ],
          [
           21.674163818359375
          ],
          [
           21.44872283935547
          ],
          [
           21.36166763305664
          ],
          [
           21.242530822753906
          ],
          [
           21.258575439453125
          ],
          [
           21.402902603149414
          ],
          [
           21.194421768188477
          ],
          [
           20.697265625
          ],
          [
           20.73850440979004
          ],
          [
           21.508291244506836
          ],
          [
           21.418949127197266
          ],
          [
           21.664087295532227
          ],
          [
           21.58160400390625
          ],
          [
           21.81529426574707
          ],
          [
           22.092514038085938
          ],
          [
           22.429288864135742
          ],
          [
           22.823347091674805
          ],
          [
           23.004344940185547
          ],
          [
           22.990598678588867
          ],
          [
           22.878334045410156
          ],
          [
           22.557592391967773
          ],
          [
           22.38805389404297
          ],
          [
           22.43387222290039
          ],
          [
           22.596540451049805
          ],
          [
           22.688190460205078
          ],
          [
           22.66756248474121
          ],
          [
           22.83022689819336
          ],
          [
           22.642358779907227
          ],
          [
           22.30099105834961
          ],
          [
           22.328489303588867
          ],
          [
           22.255170822143555
          ],
          [
           22.34910774230957
          ],
          [
           21.84049415588379
          ],
          [
           21.78779411315918
          ],
          [
           21.97337532043457
          ],
          [
           21.890899658203125
          ],
          [
           22.01690673828125
          ],
          [
           21.398326873779297
          ],
          [
           21.08673858642578
          ],
          [
           21.441850662231445
          ],
          [
           21.627429962158203
          ],
          [
           21.90235137939453
          ],
          [
           21.968793869018555
          ],
          [
           21.76259994506836
          ],
          [
           21.88631820678711
          ],
          [
           21.980247497558594
          ],
          [
           22.1497859954834
          ],
          [
           22.218517303466797
          ],
          [
           22.319316864013672
          ],
          [
           22.193309783935547
          ],
          [
           22.63319206237793
          ],
          [
           22.63089942932129
          ],
          [
           22.871463775634766
          ],
          [
           22.880615234375
          ],
          [
           22.901243209838867
          ],
          [
           22.77982521057129
          ],
          [
           22.603410720825195
          ],
          [
           22.30099105834961
          ],
          [
           22.147499084472656
          ],
          [
           23.586271286010742
          ],
          [
           23.904720306396484
          ],
          [
           23.87493896484375
          ],
          [
           24.29649543762207
          ],
          [
           23.93678855895996
          ],
          [
           24.236923217773438
          ],
          [
           24.386648178100586
          ],
          [
           24.757505416870117
          ],
          [
           24.96251106262207
          ],
          [
           25.063865661621094
          ],
          [
           24.87728500366211
          ],
          [
           24.861160278320312
          ],
          [
           24.918743133544922
          ],
          [
           25.218196868896484
          ],
          [
           25.195161819458008
          ],
          [
           25.158308029174805
          ],
          [
           25.12605857849121
          ],
          [
           25.1905517578125
          ],
          [
           24.994760513305664
          ],
          [
           25.073076248168945
          ],
          [
           24.88419532775879
          ],
          [
           24.778236389160156
          ],
          [
           24.633121490478516
          ],
          [
           24.605478286743164
          ],
          [
           24.416584014892578
          ],
          [
           24.43963050842285
          ],
          [
           24.584741592407227
          ],
          [
           24.815095901489258
          ],
          [
           24.80817985534668
          ],
          [
           24.960203170776367
          ],
          [
           24.3060245513916
          ],
          [
           23.75550079345703
          ],
          [
           24.28759765625
          ],
          [
           24.865766525268555
          ],
          [
           25.745683670043945
          ],
          [
           26.620990753173828
          ],
          [
           26.471267700195312
          ],
          [
           26.16260528564453
          ],
          [
           26.160301208496094
          ],
          [
           26.155702590942383
          ],
          [
           26.40216636657715
          ],
          [
           25.96221351623535
          ],
          [
           26.001371383666992
          ],
          [
           26.049745559692383
          ],
          [
           26.247835159301758
          ],
          [
           25.840126037597656
          ],
          [
           26.040525436401367
          ],
          [
           25.918445587158203
          ],
          [
           26.02901268005371
          ],
          [
           26.040525436401367
          ],
          [
           26.23401641845703
          ],
          [
           26.273176193237305
          ],
          [
           26.73155975341797
          ],
          [
           26.789148330688477
          ],
          [
           27.028701782226562
          ],
          [
           26.945785522460938
          ],
          [
           27.095502853393555
          ],
          [
           27.077085494995117
          ],
          [
           27.05865478515625
          ],
          [
           26.978029251098633
          ],
          [
           26.964208602905273
          ],
          [
           26.858251571655273
          ],
          [
           27.100112915039062
          ],
          [
           27.238319396972656
          ],
          [
           26.6256046295166
          ],
          [
           26.36992073059082
          ],
          [
           26.194862365722656
          ],
          [
           26.153398513793945
          ],
          [
           25.681188583374023
          ],
          [
           25.704219818115234
          ],
          [
           25.42870330810547
          ],
          [
           25.199487686157227
          ],
          [
           25.562990188598633
          ],
          [
           25.713481903076172
          ],
          [
           25.671804428100586
          ],
          [
           24.95638656616211
          ],
          [
           25.104570388793945
          ],
          [
           24.474807739257812
          ],
          [
           24.798946380615234
          ],
          [
           25.46575164794922
          ],
          [
           25.45648765563965
          ],
          [
           25.481958389282227
          ],
          [
           25.868610382080078
          ],
          [
           25.88481903076172
          ],
          [
           25.75284194946289
          ],
          [
           25.882505416870117
          ],
          [
           25.831565856933594
          ],
          [
           25.806093215942383
          ],
          [
           25.588459014892578
          ],
          [
           25.349985122680664
          ],
          [
           25.44491195678711
          ],
          [
           25.26200294494629
          ],
          [
           25.45648765563965
          ],
          [
           25.706539154052734
          ],
          [
           25.95890235900879
          ],
          [
           26.382598876953125
          ],
          [
           26.23210906982422
          ],
          [
           26.669692993164062
          ],
          [
           26.669692993164062
          ],
          [
           26.815555572509766
          ],
          [
           26.85028839111328
          ],
          [
           27.00540542602539
          ],
          [
           27.077186584472656
          ],
          [
           27.102649688720703
          ],
          [
           26.924379348754883
          ],
          [
           26.97762107849121
          ],
          [
           27.148958206176758
          ],
          [
           27.033191680908203
          ],
          [
           27.026248931884766
          ],
          [
           26.815555572509766
          ],
          [
           26.89196014404297
          ],
          [
           26.86186408996582
          ],
          [
           26.998458862304688
          ],
          [
           27.29945182800293
          ],
          [
           27.549503326416016
          ],
          [
           27.577280044555664
          ],
          [
           27.725461959838867
          ],
          [
           27.60969352722168
          ],
          [
           27.561077117919922
          ],
          [
           27.783344268798828
          ],
          [
           27.78101921081543
          ],
          [
           27.732402801513672
          ],
          [
           27.783344268798828
          ],
          [
           27.801860809326172
          ],
          [
           27.776399612426758
          ],
          [
           28.218616485595703
          ],
          [
           28.232501983642578
          ],
          [
           28.234825134277344
          ],
          [
           28.160736083984375
          ],
          [
           28.095905303955078
          ],
          [
           29.809206008911133
          ],
          [
           29.758277893066406
          ],
          [
           29.885616302490234
          ],
          [
           30.165760040283203
          ],
          [
           30.452869415283203
          ],
          [
           30.570940017700195
          ],
          [
           30.791841506958008
          ],
          [
           30.72208023071289
          ],
          [
           30.994150161743164
          ],
          [
           31.396432876586914
          ],
          [
           31.510372161865234
          ],
          [
           31.473161697387695
          ],
          [
           31.559188842773438
          ],
          [
           31.787076950073242
          ],
          [
           31.882413864135742
          ],
          [
           31.747562408447266
          ],
          [
           31.77776336669922
          ],
          [
           31.84055519104004
          ],
          [
           31.854516983032227
          ],
          [
           32.50559997558594
          ],
          [
           32.31260681152344
          ],
          [
           32.5032844543457
          ],
          [
           32.40096664428711
          ],
          [
           32.44282150268555
          ],
          [
           32.3218994140625
          ],
          [
           32.24748992919922
          ],
          [
           32.354461669921875
          ],
          [
           32.368412017822266
          ],
          [
           32.31957244873047
          ],
          [
           32.66139221191406
          ],
          [
           32.71487808227539
          ],
          [
           32.552101135253906
          ],
          [
           32.8939323425293
          ],
          [
           32.5172233581543
          ],
          [
           32.8846321105957
          ],
          [
           32.76836013793945
          ],
          [
           32.703250885009766
          ],
          [
           32.759063720703125
          ],
          [
           33.43806076049805
          ],
          [
           33.5124626159668
          ],
          [
           33.468284606933594
          ],
          [
           33.4055061340332
          ],
          [
           33.4148063659668
          ],
          [
           33.66360855102539
          ],
          [
           33.48921585083008
          ],
          [
           33.4055061340332
          ],
          [
           33.331092834472656
          ],
          [
           33.29155731201172
          ],
          [
           32.9334602355957
          ],
          [
           32.97298812866211
          ],
          [
           32.798587799072266
          ],
          [
           32.97996520996094
          ],
          [
           32.833465576171875
          ],
          [
           32.712554931640625
          ],
          [
           33.12181091308594
          ],
          [
           33.08228302001953
          ],
          [
           33.40085220336914
          ],
          [
           33.6077995300293
          ],
          [
           33.41015625
          ],
          [
           33.43572235107422
          ],
          [
           33.403167724609375
          ],
          [
           34.084495544433594
          ],
          [
           34.300743103027344
          ],
          [
           34.196102142333984
          ],
          [
           34.07286071777344
          ],
          [
           34.63793182373047
          ],
          [
           35.57966995239258
          ],
          [
           35.807559967041016
          ],
          [
           35.63779830932617
          ],
          [
           35.946014404296875
          ],
          [
           36.44801712036133
          ],
          [
           36.354610443115234
          ],
          [
           36.3009147644043
          ],
          [
           35.082096099853516
          ],
          [
           35.61678695678711
          ],
          [
           35.73819351196289
          ],
          [
           35.955352783203125
          ],
          [
           35.910980224609375
          ],
          [
           35.80358123779297
          ],
          [
           35.92732620239258
          ],
          [
           35.86660385131836
          ],
          [
           35.88063430786133
          ],
          [
           35.66815948486328
          ],
          [
           35.766231536865234
          ],
          [
           36.29624557495117
          ],
          [
           35.94133758544922
          ],
          [
           36.0627555847168
          ],
          [
           36.27756881713867
          ],
          [
           36.18885040283203
          ],
          [
           34.78554916381836
          ],
          [
           33.95431900024414
          ],
          [
           34.22751998901367
          ],
          [
           33.893619537353516
          ],
          [
           33.690486907958984
          ],
          [
           33.21883773803711
          ],
          [
           34.16914367675781
          ],
          [
           33.85860061645508
          ],
          [
           34.059391021728516
          ],
          [
           34.00336837768555
          ],
          [
           34.15513229370117
          ],
          [
           34.04771041870117
          ],
          [
           33.559730529785156
          ],
          [
           34.0500602722168
          ],
          [
           33.54804992675781
          ],
          [
           33.627445220947266
          ],
          [
           33.506019592285156
          ],
          [
           33.64377975463867
          ],
          [
           33.32624053955078
          ],
          [
           33.664794921875
          ],
          [
           33.870269775390625
          ],
          [
           33.980003356933594
          ],
          [
           34.029056549072266
          ],
          [
           34.50303649902344
          ],
          [
           34.799560546875
          ],
          [
           34.92098617553711
          ],
          [
           35.04239273071289
          ],
          [
           35.26187515258789
          ],
          [
           35.10310745239258
          ],
          [
           35.086761474609375
          ],
          [
           35.511714935302734
          ],
          [
           35.663490295410156
          ],
          [
           35.831600189208984
          ],
          [
           35.154476165771484
          ],
          [
           34.906978607177734
          ],
          [
           34.72718048095703
          ],
          [
           35.035396575927734
          ],
          [
           36.69084548950195
          ],
          [
           36.32426452636719
          ],
          [
           36.515724182128906
          ],
          [
           37.08077621459961
          ],
          [
           37.3773193359375
          ],
          [
           37.60614013671875
          ],
          [
           36.40831756591797
          ],
          [
           36.91463088989258
          ],
          [
           37.47018814086914
          ],
          [
           37.88039016723633
          ],
          [
           37.72802734375
          ],
          [
           37.003700256347656
          ],
          [
           36.919307708740234
          ],
          [
           36.851341247558594
          ],
          [
           37.45377731323242
          ],
          [
           37.50065231323242
          ],
          [
           37.3342170715332
          ],
          [
           37.4725341796875
          ],
          [
           37.84990692138672
          ],
          [
           38.187461853027344
          ],
          [
           38.29060745239258
          ],
          [
           38.442970275878906
          ],
          [
           38.45469665527344
          ],
          [
           37.9929084777832
          ],
          [
           37.95305252075195
          ],
          [
           37.800689697265625
          ],
          [
           37.1842041015625
          ],
          [
           37.85696792602539
          ],
          [
           37.7069206237793
          ],
          [
           37.42329406738281
          ],
          [
           37.10215759277344
          ],
          [
           37.47721481323242
          ],
          [
           37.19358444213867
          ],
          [
           37.2076416015625
          ],
          [
           36.58411407470703
          ],
          [
           35.955909729003906
          ],
          [
           35.604286193847656
          ],
          [
           35.29018783569336
          ],
          [
           35.89729690551758
          ],
          [
           36.152801513671875
          ],
          [
           35.93011474609375
          ],
          [
           36.127017974853516
          ],
          [
           36.05434799194336
          ],
          [
           36.21140670776367
          ],
          [
           35.97699737548828
          ],
          [
           36.424713134765625
          ],
          [
           36.40362548828125
          ],
          [
           36.53019714355469
          ],
          [
           36.54426193237305
          ],
          [
           36.696632385253906
          ],
          [
           36.56770706176758
          ],
          [
           36.799766540527344
          ],
          [
           37.47721481323242
          ],
          [
           37.61552047729492
          ],
          [
           37.44907760620117
          ],
          [
           36.563026428222656
          ],
          [
           36.62630081176758
          ],
          [
           36.6075553894043
          ],
          [
           36.82556915283203
          ],
          [
           36.663814544677734
          ],
          [
           36.898223876953125
          ],
          [
           38.220279693603516
          ],
          [
           39.080562591552734
          ],
          [
           39.62439727783203
          ],
          [
           39.120426177978516
          ],
          [
           39.406394958496094
          ],
          [
           40.43544387817383
          ],
          [
           40.84566879272461
          ],
          [
           40.976924896240234
          ],
          [
           41.3121337890625
          ],
          [
           41.227745056152344
          ],
          [
           41.091285705566406
          ],
          [
           40.9266242980957
          ],
          [
           40.307918548583984
          ],
          [
           39.776241302490234
          ],
          [
           40.25145721435547
          ],
          [
           40.027957916259766
          ],
          [
           39.98796463012695
          ],
          [
           40.73136520385742
          ],
          [
           41.15952682495117
          ],
          [
           41.161888122558594
          ],
          [
           40.9548454284668
          ],
          [
           40.714900970458984
          ],
          [
           39.87035369873047
          ],
          [
           40.42789840698242
          ],
          [
           40.239688873291016
          ],
          [
           39.945621490478516
          ],
          [
           39.907989501953125
          ],
          [
           39.75977325439453
          ],
          [
           39.83271026611328
          ],
          [
           39.8444709777832
          ],
          [
           40.62080001831055
          ],
          [
           40.39260482788086
          ],
          [
           40.526702880859375
          ],
          [
           40.514949798583984
          ],
          [
           40.9266242980957
          ],
          [
           41.50300216674805
          ],
          [
           41.06071853637695
          ],
          [
           41.01601791381836
          ],
          [
           41.171287536621094
          ],
          [
           41.171287536621094
          ],
          [
           40.126766204833984
          ],
          [
           40.13383865356445
          ],
          [
           40.24674987792969
          ],
          [
           39.8115348815918
          ],
          [
           40.52433776855469
          ],
          [
           40.517295837402344
          ],
          [
           40.70549392700195
          ],
          [
           41.168941497802734
          ],
          [
           41.01601791381836
          ],
          [
           41.01131820678711
          ],
          [
           41.00190734863281
          ],
          [
           41.23479461669922
          ],
          [
           41.66059875488281
          ],
          [
           41.448890686035156
          ],
          [
           42.13345718383789
          ],
          [
           42.171104431152344
          ],
          [
           41.98290252685547
          ],
          [
           41.639434814453125
          ],
          [
           41.648834228515625
          ],
          [
           40.985435485839844
          ],
          [
           40.253807067871094
          ],
          [
           40.34790802001953
          ],
          [
           39.51277542114258
          ],
          [
           39.27987289428711
          ],
          [
           39.38807678222656
          ],
          [
           39.47041702270508
          ],
          [
           37.75779724121094
          ],
          [
           36.81444549560547
          ],
          [
           38.35298538208008
          ],
          [
           37.531951904296875
          ],
          [
           36.49919891357422
          ],
          [
           36.945640563964844
          ],
          [
           38.43375778198242
          ],
          [
           38.81877899169922
          ],
          [
           39.53450393676758
          ],
          [
           40.861995697021484
          ],
          [
           40.72971725463867
          ],
          [
           40.59272384643555
          ],
          [
           40.40849304199219
          ],
          [
           40.74625778198242
          ],
          [
           41.454898834228516
          ],
          [
           42.2745361328125
          ],
          [
           42.137535095214844
          ],
          [
           42.07376480102539
          ],
          [
           41.336788177490234
          ],
          [
           41.62259292602539
          ],
          [
           41.766685485839844
          ],
          [
           41.73125457763672
          ],
          [
           41.343868255615234
          ],
          [
           41.79502868652344
          ],
          [
           42.51311111450195
          ],
          [
           42.92411422729492
          ],
          [
           42.51074981689453
          ],
          [
           42.149356842041016
          ],
          [
           42.19895553588867
          ],
          [
           42.050132751464844
          ],
          [
           41.40764617919922
          ],
          [
           41.393470764160156
          ],
          [
           40.45571517944336
          ],
          [
           39.884090423583984
          ],
          [
           38.96051788330078
          ],
          [
           40.810035705566406
          ],
          [
           39.76361846923828
          ],
          [
           39.32427215576172
          ],
          [
           39.63134765625
          ],
          [
           39.37150955200195
          ],
          [
           39.77543640136719
          ],
          [
           40.536033630371094
          ],
          [
           40.81712341308594
          ],
          [
           39.77307891845703
          ],
          [
           40.167545318603516
          ],
          [
           40.92341995239258
          ],
          [
           40.732093811035156
          ],
          [
           41.1336555480957
          ],
          [
           41.27300262451172
          ],
          [
           41.530479431152344
          ],
          [
           42.10210418701172
          ],
          [
           42.00762176513672
          ],
          [
           40.81712341308594
          ],
          [
           39.14474868774414
          ],
          [
           39.0313720703125
          ],
          [
           38.48808670043945
          ],
          [
           38.65579605102539
          ],
          [
           38.790435791015625
          ],
          [
           38.34165954589844
          ],
          [
           39.036102294921875
          ],
          [
           39.94314193725586
          ],
          [
           41.707637786865234
          ],
          [
           41.783206939697266
          ],
          [
           43.42251205444336
          ],
          [
           43.73667526245117
          ],
          [
           43.94690704345703
          ],
          [
           44.25634765625
          ],
          [
           44.889381408691406
          ],
          [
           44.718666076660156
          ],
          [
           44.614322662353516
          ],
          [
           44.20885467529297
          ],
          [
           44.621437072753906
          ],
          [
           44.33926773071289
          ],
          [
           44.178016662597656
          ],
          [
           44.49102020263672
          ],
          [
           44.37958526611328
          ],
          [
           44.664119720458984
          ],
          [
           44.614322662353516
          ],
          [
           44.71628952026367
          ],
          [
           44.5550422668457
          ],
          [
           44.460201263427734
          ],
          [
           44.31081771850586
          ],
          [
           45.109920501708984
          ],
          [
           45.48691940307617
          ],
          [
           45.83787536621094
          ],
          [
           45.99673080444336
          ],
          [
           45.873443603515625
          ],
          [
           45.45609664916992
          ],
          [
           45.34465408325195
          ],
          [
           45.59363555908203
          ],
          [
           45.218990325927734
          ],
          [
           45.242698669433594
          ],
          [
           44.77793884277344
          ],
          [
           44.754234313964844
          ],
          [
           44.03101348876953
          ],
          [
           44.223060607910156
          ],
          [
           43.97647476196289
          ],
          [
           43.84842300415039
          ],
          [
           43.196353912353516
          ],
          [
           43.73222732543945
          ],
          [
           43.66820526123047
          ],
          [
           43.98595428466797
          ],
          [
           43.89348602294922
          ],
          [
           44.384315490722656
          ],
          [
           43.61131286621094
          ],
          [
           43.962242126464844
          ],
          [
           44.57164001464844
          ],
          [
           45.19052505493164
          ],
          [
           45.135990142822266
          ],
          [
           44.55030822753906
          ],
          [
           45.29723358154297
          ],
          [
           45.36836242675781
          ],
          [
           45.26877212524414
          ],
          [
           45.396820068359375
          ],
          [
           45.14784622192383
          ],
          [
           45.49878692626953
          ],
          [
           45.39445114135742
          ],
          [
           45.43476867675781
          ],
          [
           45.764366149902344
          ],
          [
           46.195919036865234
          ],
          [
           46.05128479003906
          ],
          [
           45.28538131713867
          ],
          [
           45.03166580200195
          ],
          [
           45.121761322021484
          ],
          [
           47.77988815307617
          ],
          [
           49.17653274536133
          ],
          [
           49.31881332397461
          ],
          [
           49.574886322021484
          ],
          [
           49.11013412475586
          ],
          [
           49.143333435058594
          ],
          [
           49.52983093261719
          ],
          [
           49.382320404052734
          ],
          [
           49.70116424560547
          ],
          [
           49.91057205200195
          ],
          [
           50.02716827392578
          ],
          [
           50.76006317138672
          ],
          [
           51.77372741699219
          ],
          [
           51.269287109375
          ],
          [
           51.16933822631836
          ],
          [
           51.17171096801758
          ],
          [
           51.27641677856445
          ],
          [
           51.435848236083984
          ],
          [
           51.85940933227539
          ],
          [
           52.27819061279297
          ],
          [
           53.058685302734375
          ],
          [
           53.54648208618164
          ],
          [
           54.165164947509766
          ],
          [
           54.33887481689453
          ],
          [
           53.984310150146484
          ],
          [
           53.087242126464844
          ],
          [
           52.65892028808594
          ],
          [
           51.952205657958984
          ],
          [
           53.26570510864258
          ],
          [
           52.604190826416016
          ],
          [
           53.87486267089844
          ],
          [
           53.2633171081543
          ],
          [
           51.84511947631836
          ],
          [
           51.93077850341797
          ],
          [
           51.96171951293945
          ],
          [
           52.35671615600586
          ],
          [
           51.79277801513672
          ],
          [
           52.53756332397461
          ],
          [
           52.87069320678711
          ],
          [
           52.44953155517578
          ],
          [
           53.52745056152344
          ],
          [
           53.715431213378906
          ],
          [
           54.077110290527344
          ],
          [
           54.55778884887695
          ],
          [
           55.22167205810547
          ],
          [
           54.250823974609375
          ],
          [
           53.37040710449219
          ],
          [
           53.246665954589844
          ],
          [
           53.984310150146484
          ],
          [
           51.48343276977539
          ],
          [
           51.02893829345703
          ],
          [
           52.851661682128906
          ],
          [
           51.72139358520508
          ],
          [
           52.861183166503906
          ],
          [
           52.632747650146484
          ],
          [
           51.402523040771484
          ],
          [
           52.18539810180664
          ],
          [
           52.50425338745117
          ],
          [
           52.99919509887695
          ],
          [
           51.181236267089844
          ],
          [
           52.3019905090332
          ],
          [
           51.46916580200195
          ],
          [
           50.503074645996094
          ],
          [
           50.75530242919922
          ],
          [
           52.07831573486328
          ],
          [
           52.87784194946289
          ],
          [
           49.37041091918945
          ],
          [
           47.9688835144043
          ],
          [
           48.487606048583984
          ],
          [
           49.95816421508789
          ],
          [
           49.78385543823242
          ],
          [
           48.823936462402344
          ],
          [
           46.36446762084961
          ],
          [
           45.9012336730957
          ],
          [
           44.60464859008789
          ],
          [
           45.7054328918457
          ],
          [
           46.2116584777832
          ],
          [
           44.380191802978516
          ],
          [
           42.259803771972656
          ],
          [
           42.212032318115234
          ],
          [
           41.139915466308594
          ],
          [
           41.696266174316406
          ],
          [
           41.60554122924805
          ],
          [
           43.20539093017578
          ],
          [
           42.873470306396484
          ],
          [
           42.641849517822266
          ],
          [
           44.131858825683594
          ],
          [
           42.19055938720703
          ],
          [
           41.720149993896484
          ],
          [
           40.23253631591797
          ],
          [
           40.497581481933594
          ],
          [
           40.265968322753906
          ],
          [
           40.37819290161133
          ],
          [
           40.819942474365234
          ],
          [
           39.5137825012207
          ],
          [
           39.14608383178711
          ],
          [
           39.65468215942383
          ],
          [
           38.41778564453125
          ],
          [
           37.448326110839844
          ],
          [
           35.99174880981445
          ],
          [
           35.06049346923828
          ],
          [
           37.52950668334961
          ],
          [
           37.285953521728516
          ],
          [
           37.305057525634766
          ],
          [
           37.665618896484375
          ],
          [
           37.70859146118164
          ],
          [
           33.95253372192383
          ],
          [
           35.401954650878906
          ],
          [
           35.323150634765625
          ],
          [
           35.99652099609375
          ],
          [
           36.60781478881836
          ],
          [
           36.724815368652344
          ],
          [
           36.3642463684082
          ],
          [
           35.81743240356445
          ],
          [
           36.550498962402344
          ],
          [
           36.99703598022461
          ],
          [
           37.21669387817383
          ],
          [
           37.44594192504883
          ],
          [
           36.60542297363281
          ],
          [
           36.75345993041992
          ],
          [
           36.462154388427734
          ],
          [
           37.67038345336914
          ],
          [
           37.32176971435547
          ],
          [
           36.934940338134766
          ],
          [
           39.45888137817383
          ],
          [
           39.74303436279297
          ],
          [
           39.76213073730469
          ],
          [
           40.891578674316406
          ],
          [
           41.5911979675293
          ],
          [
           41.60554122924805
          ],
          [
           40.81755447387695
          ],
          [
           40.865516662597656
          ],
          [
           40.6305046081543
          ],
          [
           40.980621337890625
          ],
          [
           40.81035614013672
          ],
          [
           40.959041595458984
          ],
          [
           40.86790084838867
          ],
          [
           40.990203857421875
          ],
          [
           41.25400161743164
          ],
          [
           41.021385192871094
          ],
          [
           41.47941207885742
          ],
          [
           41.781578063964844
          ],
          [
           41.8055534362793
          ],
          [
           41.93504333496094
          ],
          [
           41.52257537841797
          ],
          [
           41.95903396606445
          ],
          [
           42.170066833496094
          ],
          [
           42.09332275390625
          ],
          [
           41.85111999511719
          ],
          [
           41.36671447753906
          ],
          [
           41.465030670166016
          ],
          [
           42.90147018432617
          ],
          [
           43.383480072021484
          ],
          [
           43.57533264160156
          ],
          [
           44.05974197387695
          ],
          [
           44.632877349853516
          ],
          [
           45.088523864746094
          ],
          [
           44.73119354248047
          ],
          [
           45.122093200683594
          ],
          [
           46.7839469909668
          ],
          [
           45.815120697021484
          ],
          [
           45.26116943359375
          ],
          [
           44.793556213378906
          ],
          [
           45.19642639160156
          ],
          [
           45.256370544433594
          ],
          [
           45.55133819580078
          ],
          [
           45.860694885253906
          ],
          [
           46.52735137939453
          ],
          [
           46.84629440307617
          ],
          [
           46.92783737182617
          ],
          [
           47.24197769165039
          ],
          [
           47.98538589477539
          ],
          [
           47.84150314331055
          ],
          [
           48.11008071899414
          ],
          [
           47.70960235595703
          ],
          [
           47.69041442871094
          ],
          [
           47.7767448425293
          ],
          [
           47.78154373168945
          ],
          [
           48.711997985839844
          ],
          [
           48.88705062866211
          ],
          [
           49.04771423339844
          ],
          [
           49.755157470703125
          ],
          [
           49.67841720581055
          ],
          [
           49.22758483886719
          ],
          [
           48.99256896972656
          ],
          [
           49.066917419433594
          ],
          [
           48.1220703125
          ],
          [
           50.484169006347656
          ],
          [
           50.1556396484375
          ],
          [
           50.77913284301758
          ],
          [
           49.994964599609375
          ],
          [
           48.64725112915039
          ],
          [
           48.65684127807617
          ],
          [
           48.134056091308594
          ],
          [
           47.46723556518555
          ],
          [
           44.708465576171875
          ],
          [
           45.41621017456055
          ],
          [
           45.960262298583984
          ],
          [
           45.75804901123047
          ],
          [
           45.49806213378906
          ],
          [
           44.075347900390625
          ],
          [
           44.9202995300293
          ],
          [
           44.00070571899414
          ],
          [
           43.24964141845703
          ],
          [
           43.08354187011719
          ],
          [
           42.905399322509766
          ],
          [
           42.70077896118164
          ],
          [
           42.92224884033203
          ],
          [
           42.14468765258789
          ],
          [
           41.718597412109375
          ],
          [
           43.24483108520508
          ],
          [
           43.94294738769531
          ],
          [
           44.58810043334961
          ],
          [
           45.77490997314453
          ],
          [
           46.35987854003906
          ],
          [
           46.896705627441406
          ],
          [
           46.74745178222656
          ],
          [
           46.737823486328125
          ],
          [
           46.398399353027344
          ],
          [
           46.67523956298828
          ],
          [
           47.7729606628418
          ],
          [
           47.63334655761719
          ],
          [
           48.01610565185547
          ],
          [
           47.85240173339844
          ],
          [
           47.80426025390625
          ],
          [
           47.07966995239258
          ],
          [
           48.097957611083984
          ],
          [
           48.083518981933594
          ],
          [
           47.64537811279297
          ],
          [
           48.51923751831055
          ],
          [
           48.80329895019531
          ],
          [
           49.20772171020508
          ],
          [
           49.16437911987305
          ],
          [
           48.150917053222656
          ],
          [
           48.44461441040039
          ],
          [
           48.92365264892578
          ],
          [
           48.5673828125
          ],
          [
           48.94050979614258
          ],
          [
           49.400306701660156
          ],
          [
           49.229393005371094
          ],
          [
           48.95254898071289
          ],
          [
           49.508636474609375
          ],
          [
           48.769588470458984
          ],
          [
           49.8841667175293
          ],
          [
           50.27416229248047
          ],
          [
           50.23323440551758
          ],
          [
           49.836029052734375
          ],
          [
           50.009361267089844
          ],
          [
           50.476375579833984
          ],
          [
           50.259708404541016
          ],
          [
           51.285221099853516
          ],
          [
           50.175445556640625
          ],
          [
           49.11384201049805
          ],
          [
           46.54283905029297
          ],
          [
           47.42390441894531
          ],
          [
           47.91499710083008
          ],
          [
           48.9718017578125
          ],
          [
           48.568260192871094
          ],
          [
           48.44501495361328
          ],
          [
           50.496578216552734
          ],
          [
           48.993560791015625
          ],
          [
           48.74949264526367
          ],
          [
           49.89973068237305
          ],
          [
           50.83005905151367
          ],
          [
           50.83247756958008
          ],
          [
           51.3834228515625
          ],
          [
           51.33993148803711
          ],
          [
           48.96697998046875
          ],
          [
           49.897315979003906
          ],
          [
           49.33427810668945
          ],
          [
           49.66532897949219
          ],
          [
           50.50624465942383
          ],
          [
           50.44100570678711
          ],
          [
           49.70640182495117
          ],
          [
           50.54975128173828
          ],
          [
           51.538082122802734
          ],
          [
           51.53323745727539
          ],
          [
           51.753143310546875
          ],
          [
           52.364498138427734
          ],
          [
           54.02943801879883
          ],
          [
           53.90862274169922
          ],
          [
           52.8598747253418
          ],
          [
           53.13776397705078
          ],
          [
           53.331092834472656
          ],
          [
           53.83129119873047
          ],
          [
           53.393917083740234
          ],
          [
           52.61339569091797
          ],
          [
           52.852622985839844
          ],
          [
           52.601322174072266
          ],
          [
           53.41082763671875
          ],
          [
           53.13534927368164
          ],
          [
           52.87679672241211
          ],
          [
           54.12126922607422
          ],
          [
           54.271080017089844
          ],
          [
           52.910614013671875
          ],
          [
           53.360076904296875
          ],
          [
           54.85586166381836
          ],
          [
           54.86793899536133
          ],
          [
           54.22517395019531
          ],
          [
           54.86069107055664
          ],
          [
           55.600128173828125
          ],
          [
           57.07899475097656
          ],
          [
           56.99684143066406
          ],
          [
           56.86393356323242
          ],
          [
           56.63437271118164
          ],
          [
           56.85427474975586
          ],
          [
           57.1273307800293
          ],
          [
           58.118064880371094
          ],
          [
           57.985164642333984
          ],
          [
           58.763267517089844
          ],
          [
           58.85992431640625
          ],
          [
           59.58485412597656
          ],
          [
           60.18171691894531
          ],
          [
           58.78984832763672
          ],
          [
           58.782596588134766
          ],
          [
           60.11164474487305
          ],
          [
           61.81766891479492
          ],
          [
           62.22362518310547
          ],
          [
           62.134220123291016
          ],
          [
           62.160789489746094
          ],
          [
           62.878211975097656
          ],
          [
           63.05031204223633
          ],
          [
           63.54957962036133
          ],
          [
           63.49140167236328
          ],
          [
           64.0997543334961
          ],
          [
           63.65621566772461
          ],
          [
           64.41241455078125
          ],
          [
           64.73721313476562
          ],
          [
           64.5408706665039
          ],
          [
           63.78952407836914
          ],
          [
           63.503536224365234
          ],
          [
           63.447792053222656
          ],
          [
           64.56026458740234
          ],
          [
           64.05613708496094
          ],
          [
           64.91654968261719
          ],
          [
           64.77354431152344
          ],
          [
           64.02462768554688
          ],
          [
           62.883052825927734
          ],
          [
           63.43809127807617
          ],
          [
           64.36878967285156
          ],
          [
           65.61214447021484
          ],
          [
           64.69355773925781
          ],
          [
           65.0716552734375
          ],
          [
           65.62669372558594
          ],
          [
           65.7939453125
          ],
          [
           66.6882553100586
          ],
          [
           67.82984161376953
          ],
          [
           67.9631576538086
          ],
          [
           67.80075073242188
          ],
          [
           67.8686294555664
          ],
          [
           67.7280502319336
          ],
          [
           68.833251953125
          ],
          [
           68.898681640625
          ],
          [
           70.26567840576172
          ],
          [
           70.23900604248047
          ],
          [
           70.65589904785156
          ],
          [
           71.17212677001953
          ],
          [
           72.7960205078125
          ],
          [
           72.08829498291016
          ],
          [
           72.6627197265625
          ],
          [
           72.32099151611328
          ],
          [
           73.4843521118164
          ],
          [
           75.04521942138672
          ],
          [
           75.21487426757812
          ],
          [
           76.82178497314453
          ],
          [
           75.78443908691406
          ],
          [
           75.45967102050781
          ],
          [
           76.40491485595703
          ],
          [
           77.25077819824219
          ],
          [
           76.72725677490234
          ],
          [
           77.00117492675781
          ],
          [
           77.37197875976562
          ],
          [
           77.14898681640625
          ],
          [
           74.88040924072266
          ],
          [
           76.99871063232422
          ],
          [
           78.61048889160156
          ],
          [
           78.49658203125
          ],
          [
           75.01612854003906
          ],
          [
           74.81011962890625
          ],
          [
           77.27989196777344
          ],
          [
           77.9100341796875
          ],
          [
           78.82134246826172
          ],
          [
           77.74996185302734
          ],
          [
           78.1192398071289
          ],
          [
           77.64793395996094
          ],
          [
           79.49188995361328
          ],
          [
           78.92581176757812
          ],
          [
           78.94527435302734
          ],
          [
           77.4997329711914
          ],
          [
           78.62213134765625
          ],
          [
           77.81554412841797
          ],
          [
           76.0541763305664
          ],
          [
           72.44159698486328
          ],
          [
           69.98783874511719
          ],
          [
           71.09809875488281
          ],
          [
           66.45054626464844
          ],
          [
           66.41166687011719
          ],
          [
           72.59464263916016
          ],
          [
           70.28910827636719
          ],
          [
           73.54943084716797
          ],
          [
           71.16370391845703
          ],
          [
           70.2186508178711
          ],
          [
           64.66487121582031
          ],
          [
           69.32218170166016
          ],
          [
           66.91458892822266
          ],
          [
           60.306453704833984
          ],
          [
           67.53166198730469
          ],
          [
           58.84391403198242
          ],
          [
           61.43129348754883
          ],
          [
           59.92744827270508
          ],
          [
           59.468284606933594
          ],
          [
           55.692909240722656
          ],
          [
           54.50975036621094
          ],
          [
           59.978477478027344
          ],
          [
           59.64806365966797
          ],
          [
           62.786922454833984
          ],
          [
           60.187400817871094
          ],
          [
           61.905025482177734
          ],
          [
           61.7786979675293
          ],
          [
           58.528079986572266
          ],
          [
           59.504730224609375
          ],
          [
           58.64955520629883
          ],
          [
           63.765995025634766
          ],
          [
           63.02743911743164
          ],
          [
           64.64060974121094
          ],
          [
           65.10704040527344
          ],
          [
           66.38494873046875
          ],
          [
           69.73759460449219
          ],
          [
           69.10107421875
          ],
          [
           69.65013885498047
          ],
          [
           68.705078125
          ],
          [
           67.27899932861328
          ],
          [
           65.19937133789062
          ],
          [
           67.07733917236328
          ],
          [
           66.81739044189453
          ],
          [
           68.74638366699219
          ],
          [
           68.79499053955078
          ],
          [
           67.67984771728516
          ],
          [
           69.90282440185547
          ],
          [
           71.37748718261719
          ],
          [
           70.22835540771484
          ],
          [
           71.22199249267578
          ],
          [
           72.29095458984375
          ],
          [
           73.03680419921875
          ],
          [
           73.79236602783203
          ],
          [
           75.54875183105469
          ],
          [
           76.73754119873047
          ],
          [
           75.86056518554688
          ],
          [
           74.94462585449219
          ],
          [
           75.40503692626953
          ],
          [
           74.95921325683594
          ],
          [
           76.72535705566406
          ],
          [
           76.2820053100586
          ],
          [
           77.76554107666016
          ],
          [
           77.18576049804688
          ],
          [
           77.68272399902344
          ],
          [
           77.15652465820312
          ],
          [
           77.49271392822266
          ],
          [
           77.52682495117188
          ],
          [
           77.45130920410156
          ],
          [
           78.40380096435547
          ],
          [
           78.76673889160156
          ],
          [
           79.20036315917969
          ],
          [
           78.51828002929688
          ],
          [
           80.75455474853516
          ],
          [
           81.2320327758789
          ],
          [
           83.79716491699219
          ],
          [
           85.95304107666016
          ],
          [
           81.82642364501953
          ],
          [
           82.53286743164062
          ],
          [
           83.55355834960938
          ],
          [
           85.76790618896484
          ],
          [
           85.64852905273438
          ],
          [
           85.6826400756836
          ],
          [
           85.19300842285156
          ],
          [
           87.42198181152344
          ],
          [
           89.28797149658203
          ],
          [
           87.71187591552734
          ],
          [
           88.87629699707031
          ],
          [
           86.14549255371094
          ],
          [
           88.130859375
          ],
          [
           88.86654663085938
          ],
          [
           88.69847869873047
          ],
          [
           88.69847869873047
          ],
          [
           91.07115936279297
          ],
          [
           90.78861236572266
          ],
          [
           92.90306854248047
          ],
          [
           93.30257415771484
          ],
          [
           93.46578216552734
          ],
          [
           93.03462219238281
          ],
          [
           94.5741958618164
          ],
          [
           95.224609375
          ],
          [
           94.05286407470703
          ],
          [
           93.86286926269531
          ],
          [
           95.8409194946289
          ],
          [
           94.51815795898438
          ],
          [
           94.78368377685547
          ],
          [
           90.469482421875
          ],
          [
           90.245361328125
          ],
          [
           92.38418579101562
          ],
          [
           90.86653900146484
          ],
          [
           92.60830688476562
          ],
          [
           93.72888946533203
          ],
          [
           103.54124450683594
          ],
          [
           106.15022277832031
          ],
          [
           106.85911560058594
          ],
          [
           107.2464370727539
          ],
          [
           110.98817443847656
          ],
          [
           108.46477508544922
          ],
          [
           110.04132080078125
          ],
          [
           106.76869201660156
          ],
          [
           110.31707763671875
          ],
          [
           112.2694320678711
          ],
          [
           112.16936492919922
          ],
          [
           111.87649536132812
          ],
          [
           112.80874633789062
          ],
          [
           112.95030975341797
          ],
          [
           115.45661926269531
          ],
          [
           121.40637969970703
          ],
          [
           122.8584213256836
          ],
          [
           121.85051727294922
          ],
          [
           123.507568359375
          ],
          [
           122.03111267089844
          ],
          [
           121.83345031738281
          ],
          [
           125.96508026123047
          ],
          [
           130.98260498046875
          ],
          [
           128.2688446044922
          ],
          [
           117.99952697753906
          ],
          [
           118.07762145996094
          ],
          [
           110.13158416748047
          ],
          [
           114.52437591552734
          ],
          [
           110.78563690185547
          ],
          [
           109.33113861083984
          ],
          [
           112.61106872558594
          ],
          [
           112.78678131103516
          ],
          [
           109.4580307006836
          ],
          [
           107.71068572998047
          ],
          [
           104.29409790039062
          ],
          [
           107.45689392089844
          ],
          [
           109.14566802978516
          ],
          [
           104.56742095947266
          ],
          [
           105.64122009277344
          ],
          [
           109.60448455810547
          ],
          [
           112.22059631347656
          ],
          [
           111.37133026123047
          ],
          [
           113.05036163330078
          ],
          [
           114.00699615478516
          ],
          [
           110.32681274414062
          ],
          [
           113.7238998413086
          ],
          [
           110.46349334716797
          ],
          [
           112.33773040771484
          ],
          [
           112.23036193847656
          ],
          [
           114.18270111083984
          ],
          [
           121.43565368652344
          ],
          [
           118.21428680419922
          ],
          [
           118.30213928222656
          ],
          [
           117.83360290527344
          ],
          [
           116.18385314941406
          ],
          [
           113.21630096435547
          ],
          [
           114.70985412597656
          ],
          [
           114.08509826660156
          ],
          [
           112.99176025390625
          ],
          [
           112.29871368408203
          ],
          [
           112.30846405029297
          ],
          [
           113.82152557373047
          ],
          [
           108.55020141601562
          ],
          [
           112.57202911376953
          ],
          [
           106.26595306396484
          ],
          [
           106.1781005859375
          ],
          [
           107.80831146240234
          ],
          [
           112.21084594726562
          ],
          [
           116.19361877441406
          ],
          [
           116.06163024902344
          ],
          [
           113.74410247802734
          ],
          [
           113.4018325805664
          ],
          [
           116.8438949584961
          ],
          [
           116.57009887695312
          ],
          [
           116.61898803710938
          ],
          [
           117.6359634399414
          ],
          [
           116.74610900878906
          ],
          [
           115.41622161865234
          ],
          [
           116.0126953125
          ],
          [
           114.74150085449219
          ],
          [
           111.32878112792969
          ],
          [
           112.61956024169922
          ],
          [
           113.46052551269531
          ],
          [
           114.00811767578125
          ],
          [
           116.41363525390625
          ],
          [
           120.00236511230469
          ],
          [
           120.35440063476562
          ],
          [
           120.21749877929688
          ],
          [
           119.54276275634766
          ],
          [
           121.00955963134766
          ],
          [
           121.6256103515625
          ],
          [
           119.08318328857422
          ],
          [
           120.51084899902344
          ],
          [
           119.6992416381836
          ],
          [
           119.08318328857422
          ],
          [
           125.04810333251953
          ],
          [
           124.97964477539062
          ],
          [
           125.84993743896484
          ],
          [
           123.85511016845703
          ],
          [
           125.39031982421875
          ],
          [
           128.9595184326172
          ],
          [
           128.0598907470703
          ],
          [
           129.04751586914062
          ],
          [
           133.6630401611328
          ],
          [
           131.88330078125
          ],
          [
           130.75877380371094
          ],
          [
           129.75157165527344
          ],
          [
           126.54421997070312
          ],
          [
           128.1087646484375
          ],
          [
           123.79643249511719
          ],
          [
           128.020751953125
          ],
          [
           129.1257781982422
          ],
          [
           126.12374114990234
          ],
          [
           125.94771575927734
          ],
          [
           127.99142456054688
          ],
          [
           126.05530548095703
          ],
          [
           124.32449340820312
          ],
          [
           124.99919891357422
          ],
          [
           129.10621643066406
          ],
          [
           133.83901977539062
          ],
          [
           135.99029541015625
          ],
          [
           139.7550048828125
          ],
          [
           139.98973083496094
          ],
          [
           138.9140625
          ],
          [
           134.0541229248047
          ],
          [
           129.0377655029297
          ],
          [
           131.1695098876953
          ],
          [
           132.00067138671875
          ],
          [
           130.97393798828125
          ],
          [
           134.34747314453125
          ],
          [
           133.9312744140625
          ],
          [
           134.0782012939453
          ],
          [
           133.19680786132812
          ],
          [
           132.58963012695312
          ],
          [
           132.3350067138672
          ],
          [
           132.5700225830078
          ],
          [
           130.43515014648438
          ],
          [
           128.1337432861328
          ],
          [
           127.027099609375
          ],
          [
           127.18377685546875
          ],
          [
           123.39384460449219
          ],
          [
           123.25672912597656
          ],
          [
           122.75727844238281
          ],
          [
           118.48747253417969
          ],
          [
           118.75186920166016
          ],
          [
           125.14680480957031
          ],
          [
           122.53205108642578
          ],
          [
           119.53533172607422
          ],
          [
           117.64525604248047
          ],
          [
           118.9085693359375
          ],
          [
           113.95321655273438
          ],
          [
           118.58540344238281
          ],
          [
           117.49837493896484
          ],
          [
           119.43741607666016
          ],
          [
           118.52664184570312
          ],
          [
           121.4254379272461
          ],
          [
           122.9727554321289
          ],
          [
           122.17948150634766
          ],
          [
           118.03697967529297
          ],
          [
           117.50814819335938
          ],
          [
           120.83782958984375
          ],
          [
           120.00540161132812
          ],
          [
           117.6060791015625
          ],
          [
           118.09574890136719
          ],
          [
           118.70291137695312
          ],
          [
           118.87918090820312
          ],
          [
           117.42001342773438
          ],
          [
           119.62347412109375
          ],
          [
           120.4559097290039
          ],
          [
           123.2959213256836
          ],
          [
           123.5995101928711
          ],
          [
           125.25453186035156
          ],
          [
           127.6636734008789
          ],
          [
           130.24905395507812
          ],
          [
           128.52548217773438
          ],
          [
           131.6494598388672
          ],
          [
           129.2991180419922
          ],
          [
           131.71803283691406
          ],
          [
           131.38504028320312
          ],
          [
           132.0509796142578
          ],
          [
           130.35678100585938
          ],
          [
           130.7386932373047
          ],
          [
           129.21095275878906
          ],
          [
           131.54173278808594
          ],
          [
           131.93345642089844
          ],
          [
           131.61032104492188
          ],
          [
           130.81707763671875
          ],
          [
           130.7191162109375
          ],
          [
           128.74090576171875
          ],
          [
           129.7985382080078
          ],
          [
           125.20557403564453
          ],
          [
           125.45040130615234
          ],
          [
           127.05647277832031
          ],
          [
           127.73336029052734
          ],
          [
           124.43726348876953
          ],
          [
           123.51515197753906
          ],
          [
           120.43486785888672
          ],
          [
           122.59302520751953
          ],
          [
           125.0258560180664
          ],
          [
           123.86830139160156
          ],
          [
           122.47530364990234
          ],
          [
           122.318359375
          ],
          [
           124.88853454589844
          ],
          [
           123.04426574707031
          ],
          [
           124.6825180053711
          ],
          [
           124.48631286621094
          ],
          [
           124.43726348876953
          ],
          [
           122.89714050292969
          ],
          [
           122.23988342285156
          ],
          [
           121.91614532470703
          ],
          [
           122.68132019042969
          ],
          [
           121.19023132324219
          ],
          [
           123.49552917480469
          ],
          [
           123.50533294677734
          ],
          [
           124.32936096191406
          ],
          [
           124.71195220947266
          ],
          [
           123.71134948730469
          ],
          [
           124.92774963378906
          ],
          [
           127.99821472167969
          ],
          [
           127.17420196533203
          ],
          [
           127.67446899414062
          ],
          [
           129.28334045410156
          ],
          [
           127.97862243652344
          ],
          [
           129.78363037109375
          ],
          [
           131.43165588378906
          ],
          [
           131.15699768066406
          ],
          [
           130.87249755859375
          ],
          [
           130.57821655273438
          ],
          [
           132.21640014648438
          ],
          [
           133.73696899414062
          ],
          [
           134.35496520996094
          ],
          [
           134.65907287597656
          ],
          [
           137.29791259765625
          ],
          [
           139.3187255859375
          ],
          [
           141.82025146484375
          ],
          [
           140.51553344726562
          ],
          [
           142.3499755859375
          ],
          [
           141.75155639648438
          ],
          [
           142.86984252929688
          ],
          [
           146.3131103515625
          ],
          [
           145.65585327148438
          ],
          [
           143.60562133789062
          ],
          [
           139.74053955078125
          ],
          [
           143.37017822265625
          ],
          [
           142.6344451904297
          ],
          [
           144.00779724121094
          ],
          [
           145.7343292236328
          ],
          [
           146.15615844726562
          ],
          [
           143.9783935546875
          ],
          [
           142.22247314453125
          ],
          [
           142.86984252929688
          ],
          [
           143.08570861816406
          ],
          [
           142.75213623046875
          ],
          [
           144.55715942382812
          ],
          [
           144.15493774414062
          ],
          [
           144.26284790039062
          ],
          [
           143.5751495361328
          ],
          [
           143.5260467529297
          ],
          [
           143.04464721679688
          ],
          [
           143.30006408691406
          ],
          [
           146.27687072753906
          ],
          [
           146.4832000732422
          ],
          [
           148.4677734375
          ],
          [
           147.55406188964844
          ],
          [
           143.791259765625
          ],
          [
           144.1253204345703
          ],
          [
           145.5891876220703
          ],
          [
           147.08250427246094
          ],
          [
           146.99407958984375
          ],
          [
           145.75619506835938
          ],
          [
           144.95057678222656
          ],
          [
           145.99200439453125
          ],
          [
           150.43263244628906
          ],
          [
           149.16531372070312
          ],
          [
           149.83334350585938
          ],
          [
           150.953369140625
          ],
          [
           151.59193420410156
          ],
          [
           153.93997192382812
          ],
          [
           152.38772583007812
          ],
          [
           151.365966796875
          ],
          [
           146.35546875
          ],
          [
           146.92530822753906
          ],
          [
           145.52040100097656
          ],
          [
           146.4144287109375
          ],
          [
           146.1786346435547
          ],
          [
           143.49655151367188
          ],
          [
           140.43130493164062
          ],
          [
           140.9127197265625
          ],
          [
           143.2902374267578
          ],
          [
           144.25302124023438
          ],
          [
           144.34144592285156
          ],
          [
           142.81866455078125
          ],
          [
           139.41940307617188
          ],
          [
           140.32327270507812
          ],
          [
           139.01658630371094
          ],
          [
           140.1464080810547
          ],
          [
           136.697998046875
          ],
          [
           138.6334686279297
          ],
          [
           139.50782775878906
          ],
          [
           140.77517700195312
          ],
          [
           140.39202880859375
          ],
          [
           140.30360412597656
          ],
          [
           139.02642822265625
          ],
          [
           138.43695068359375
          ],
          [
           141.23692321777344
          ],
          [
           142.29795837402344
          ],
          [
           143.97796630859375
          ],
          [
           146.14918518066406
          ],
          [
           146.64041137695312
          ],
          [
           146.8565216064453
          ],
          [
           146.08041381835938
          ],
          [
           146.03128051757812
          ],
          [
           146.69935607910156
          ],
          [
           146.2375946044922
          ],
          [
           149.89230346679688
          ],
          [
           147.17092895507812
          ],
          [
           146.34568786621094
          ],
          [
           147.38706970214844
          ],
          [
           148.8312530517578
          ],
          [
           148.31060791015625
          ],
          [
           148.84185791015625
          ],
          [
           148.01541137695312
          ],
          [
           148.37945556640625
          ],
          [
           145.5360107421875
          ],
          [
           145.48680114746094
          ],
          [
           147.5726318359375
          ],
          [
           147.58245849609375
          ],
          [
           148.56637573242188
          ],
          [
           151.01625061035156
          ],
          [
           155.32566833496094
          ],
          [
           157.96246337890625
          ],
          [
           158.42491149902344
          ],
          [
           158.80859375
          ],
          [
           159.33004760742188
          ],
          [
           154.28273010253906
          ],
          [
           157.657470703125
          ],
          [
           162.63589477539062
          ],
          [
           162.11444091796875
          ],
          [
           161.12069702148438
          ],
          [
           159.2316436767578
          ],
          [
           162.65557861328125
          ],
          [
           168.42111206054688
          ],
          [
           172.25831604003906
          ],
          [
           171.7466583251953
          ],
          [
           176.557861328125
          ],
          [
           172.9076385498047
          ],
          [
           171.52037048339844
          ],
          [
           176.41026306152344
          ],
          [
           169.48374938964844
          ],
          [
           168.3817901611328
          ],
          [
           167.01419067382812
          ],
          [
           170.2019805908203
          ],
          [
           172.80926513671875
          ],
          [
           173.43896484375
          ],
          [
           177.42367553710938
          ],
          [
           176.40042114257812
          ],
          [
           176.489013671875
          ],
          [
           175.32798767089844
          ],
          [
           174.7081756591797
          ],
          [
           179.0765838623047
          ],
          [
           176.80381774902344
          ],
          [
           172.10086059570312
          ],
          [
           169.22793579101562
          ],
          [
           169.3951873779297
          ],
          [
           169.4148712158203
          ],
          [
           172.25831604003906
          ],
          [
           172.70103454589844
          ],
          [
           169.4148712158203
          ],
          [
           170.28070068359375
          ],
          [
           167.0634002685547
          ],
          [
           163.55091857910156
          ],
          [
           161.858642578125
          ],
          [
           159.79246520996094
          ],
          [
           159.0152130126953
          ],
          [
           157.20486450195312
          ],
          [
           157.1163330078125
          ],
          [
           156.65390014648438
          ],
          [
           167.58480834960938
          ],
          [
           171.96311950683594
          ],
          [
           171.79583740234375
          ],
          [
           173.00604248046875
          ],
          [
           170.1134033203125
          ],
          [
           169.82772827148438
          ],
          [
           169.1085968017578
          ],
          [
           172.23146057128906
          ],
          [
           173.65994262695312
          ],
          [
           169.5617218017578
          ],
          [
           166.1334686279297
          ],
          [
           166.36993408203125
          ],
          [
           170.22177124023438
          ],
          [
           169.9853515625
          ],
          [
           166.36993408203125
          ],
          [
           164.81338500976562
          ],
          [
           161.877685546875
          ],
          [
           157.69085693359375
          ],
          [
           160.32115173339844
          ],
          [
           162.39979553222656
          ],
          [
           162.66580200195312
          ],
          [
           160.7743377685547
          ],
          [
           164.0843963623047
          ],
          [
           163.75929260253906
          ],
          [
           160.74478149414062
          ],
          [
           156.9322967529297
          ],
          [
           155.09994506835938
          ],
          [
           160.52804565429688
          ],
          [
           156.16390991210938
          ],
          [
           152.4302215576172
          ],
          [
           148.38128662109375
          ],
          [
           152.78485107421875
          ],
          [
           157.21800231933594
          ],
          [
           158.23265075683594
          ],
          [
           161.54270935058594
          ],
          [
           162.9219207763672
          ],
          [
           166.31080627441406
          ],
          [
           167.68014526367188
          ],
          [
           171.4827880859375
          ],
          [
           172.12310791015625
          ],
          [
           172.99002075195312
          ],
          [
           176.30007934570312
          ],
          [
           175.1277618408203
          ],
          [
           172.01470947265625
          ],
          [
           171.71922302246094
          ],
          [
           175.787841796875
          ],
          [
           172.4580078125
          ],
          [
           169.2760772705078
          ],
          [
           169.58143615722656
          ],
          [
           167.56192016601562
          ],
          [
           163.28640747070312
          ],
          [
           165.16802978515625
          ],
          [
           167.8672637939453
          ],
          [
           162.833251953125
          ],
          [
           162.61651611328125
          ],
          [
           164.91188049316406
          ],
          [
           164.7444305419922
          ],
          [
           163.94647216796875
          ],
          [
           159.38525390625
          ],
          [
           160.45909118652344
          ],
          [
           154.46945190429688
          ],
          [
           154.2428741455078
          ],
          [
           161.207763671875
          ],
          [
           155.3068389892578
          ],
          [
           155.6122283935547
          ],
          [
           157.10960388183594
          ],
          [
           163.5524139404297
          ],
          [
           154.4398956298828
          ],
          [
           155.16998291015625
          ],
          [
           150.01998901367188
          ],
          [
           152.4371337890625
          ],
          [
           144.53457641601562
          ],
          [
           140.6474609375
          ],
          [
           145.13641357421875
          ],
          [
           143.58746337890625
          ],
          [
           147.2378387451172
          ],
          [
           138.9307861328125
          ],
          [
           135.50733947753906
          ],
          [
           135.74412536621094
          ],
          [
           141.1900634765625
          ],
          [
           138.4769744873047
          ],
          [
           138.63482666015625
          ],
          [
           141.85108947753906
          ],
          [
           147.63246154785156
          ],
          [
           146.8432159423828
          ],
          [
           146.71495056152344
          ],
          [
           149.18141174316406
          ],
          [
           143.42962646484375
          ],
          [
           144.1793975830078
          ],
          [
           146.71495056152344
          ],
          [
           145.97500610351562
          ],
          [
           140.7263641357422
          ],
          [
           135.29029846191406
          ],
          [
           130.11073303222656
          ],
          [
           130.9789276123047
          ],
          [
           133.6130828857422
          ],
          [
           128.31512451171875
          ],
          [
           129.79502868652344
          ],
          [
           134.0471954345703
          ],
          [
           133.53416442871094
          ],
          [
           136.41500854492188
          ],
          [
           139.759521484375
          ],
          [
           139.759521484375
          ],
          [
           135.5961151123047
          ],
          [
           137.36212158203125
          ],
          [
           134.8857879638672
          ],
          [
           137.06614685058594
          ],
          [
           139.66085815429688
          ],
          [
           141.00259399414062
          ],
          [
           144.3865966796875
          ],
          [
           145.06732177734375
          ],
          [
           142.92645263671875
          ],
          [
           143.90313720703125
          ],
          [
           143.5381622314453
          ],
          [
           146.4781494140625
          ],
          [
           148.15533447265625
          ],
          [
           145.09693908691406
          ],
          [
           148.97421264648438
          ],
          [
           150.98683166503906
          ],
          [
           153.26583862304688
          ],
          [
           152.02276611328125
          ],
          [
           150.89805603027344
          ],
          [
           149.56619262695312
          ],
          [
           154.68655395507812
          ],
          [
           155.23904418945312
          ],
          [
           160.3297882080078
          ],
          [
           159.34323120117188
          ],
          [
           157.8633575439453
          ],
          [
           163.90122985839844
          ],
          [
           163.5855255126953
          ],
          [
           163.35830688476562
          ],
          [
           162.8840789794922
          ],
          [
           162.9334716796875
          ],
          [
           167.20144653320312
          ],
          [
           166.46047973632812
          ],
          [
           170.02699279785156
          ],
          [
           171.10389709472656
          ],
          [
           170.94580078125
          ],
          [
           172.44747924804688
          ],
          [
           172.0522918701172
          ],
          [
           169.45399475097656
          ],
          [
           165.55154418945312
          ],
          [
           165.2156524658203
          ],
          [
           165.51205444335938
          ],
          [
           167.98191833496094
          ],
          [
           161.6491241455078
          ],
          [
           159.43614196777344
          ],
          [
           156.9958953857422
          ],
          [
           155.3262481689453
          ],
          [
           156.0572967529297
          ],
          [
           153.93321228027344
          ],
          [
           152.6686248779297
          ],
          [
           154.08139038085938
          ],
          [
           152.59945678710938
          ],
          [
           155.47442626953125
          ],
          [
           161.46141052246094
          ],
          [
           151.98695373535156
          ],
          [
           153.43923950195312
          ],
          [
           150.53465270996094
          ],
          [
           148.88475036621094
          ],
          [
           152.61923217773438
          ],
          [
           155.0100555419922
          ],
          [
           151.8683624267578
          ],
          [
           150.9001922607422
          ],
          [
           148.6179962158203
          ],
          [
           148.95391845703125
          ],
          [
           149.9320068359375
          ],
          [
           148.0350799560547
          ],
          [
           140.76377868652344
          ],
          [
           136.53530883789062
          ],
          [
           140.734130859375
          ],
          [
           144.34017944335938
          ],
          [
           144.63653564453125
          ],
          [
           143.67823791503906
          ],
          [
           138.40255737304688
          ],
          [
           138.72857666015625
          ],
          [
           137.30592346191406
          ],
          [
           136.6736602783203
          ],
          [
           141.26763916015625
          ],
          [
           136.7131805419922
          ],
          [
           140.6946258544922
          ],
          [
           142.0185089111328
          ],
          [
           142.12716674804688
          ],
          [
           141.66282653808594
          ],
          [
           145.49609375
          ],
          [
           147.64981079101562
          ],
          [
           150.50503540039062
          ],
          [
           147.55101013183594
          ],
          [
           143.05584716796875
          ],
          [
           153.86407470703125
          ],
          [
           151.4929656982422
          ],
          [
           148.83535766601562
          ],
          [
           143.2830352783203
          ],
          [
           137.2071533203125
          ],
          [
           136.93994140625
          ],
          [
           137.4743194580078
          ],
          [
           138.04830932617188
          ],
          [
           133.46646118164062
          ],
          [
           145.3415985107422
          ],
          [
           148.14215087890625
          ],
          [
           146.73692321777344
          ],
          [
           148.47860717773438
          ],
          [
           147.24163818359375
          ],
          [
           149.1515350341797
          ],
          [
           149.71559143066406
          ],
          [
           146.4697265625
          ],
          [
           148.61712646484375
          ],
          [
           149.49790954589844
          ],
          [
           146.56871032714844
          ],
          [
           142.7191925048828
          ],
          [
           139.700927734375
          ],
          [
           146.48953247070312
          ],
          [
           146.76661682128906
          ],
          [
           146.27183532714844
          ],
          [
           145.10411071777344
          ],
          [
           141.42282104492188
          ],
          [
           139.47332763671875
          ],
          [
           141.16549682617188
          ],
          [
           140.6806182861328
          ],
          [
           142.9863739013672
          ],
          [
           143.95619201660156
          ],
          [
           141.71969604492188
          ],
          [
           135.07949829101562
          ],
          [
           133.1102294921875
          ],
          [
           130.99249267578125
          ],
          [
           130.92323303222656
          ],
          [
           134.0404052734375
          ],
          [
           130.8539581298828
          ],
          [
           130.48776245117188
          ],
          [
           128.6768341064453
          ],
          [
           124.72836303710938
          ],
          [
           128.26119995117188
          ],
          [
           128.577880859375
          ],
          [
           123.7684555053711
          ],
          [
           125.04503631591797
          ],
          [
           123.71897888183594
          ],
          [
           128.27108764648438
          ],
          [
           128.7955780029297
          ],
          [
           129.3695526123047
          ],
          [
           132.10084533691406
          ],
          [
           132.02166748046875
          ],
          [
           133.3576202392578
          ],
          [
           134.5253448486328
          ],
          [
           133.8029327392578
          ],
          [
           133.8623046875
          ],
          [
           136.43524169921875
          ],
          [
           139.6415252685547
          ],
          [
           141.0467529296875
          ],
          [
           140.3837432861328
          ],
          [
           142.4619140625
          ],
          [
           144.41136169433594
          ],
          [
           141.5118865966797
          ],
          [
           142.7884521484375
          ],
          [
           143.91656494140625
          ],
          [
           149.25050354003906
          ],
          [
           152.89218139648438
          ],
          [
           150.1510009765625
          ],
          [
           153.04063415527344
          ],
          [
           150.33901977539062
          ],
          [
           149.2999725341797
          ],
          [
           149.6666717529297
          ],
          [
           152.4814453125
          ],
          [
           151.83718872070312
          ],
          [
           153.9482421875
          ],
          [
           152.3426513671875
          ],
          [
           151.1929931640625
          ],
          [
           147.1591796875
          ],
          [
           147.58535766601562
          ],
          [
           148.0709991455078
          ],
          [
           145.4049530029297
          ],
          [
           146.6041717529297
          ],
          [
           146.0987091064453
          ],
          [
           144.0173797607422
          ],
          [
           144.612060546875
          ],
          [
           149.6865234375
          ],
          [
           152.46160888671875
          ],
          [
           150.25144958496094
          ],
          [
           151.5101318359375
          ],
          [
           149.2504119873047
          ],
          [
           147.17901611328125
          ],
          [
           149.13150024414062
          ],
          [
           151.2326202392578
          ],
          [
           151.6290740966797
          ],
          [
           154.46365356445312
          ],
          [
           153.62118530273438
          ],
          [
           155.9998321533203
          ],
          [
           157.8631134033203
          ],
          [
           156.42599487304688
          ],
          [
           157.51620483398438
          ],
          [
           158.82449340820312
          ],
          [
           156.87200927734375
          ],
          [
           156.24761962890625
          ],
          [
           159.33985900878906
          ],
          [
           160.91571044921875
          ],
          [
           163.43310546875
          ],
          [
           164.69183349609375
          ],
          [
           164.15664672851562
          ],
          [
           162.3032684326172
          ],
          [
           163.1952667236328
          ],
          [
           160.58863830566406
          ],
          [
           159.36959838867188
          ],
          [
           158.67584228515625
          ],
          [
           164.08724975585938
          ],
          [
           163.74037170410156
          ],
          [
           163.7601776123047
          ],
          [
           164.98916625976562
          ],
          [
           166.13885498046875
          ],
          [
           165.16757202148438
          ],
          [
           163.55206298828125
          ],
          [
           163.85928344726562
          ],
          [
           162.31317138671875
          ],
          [
           162.3032684326172
          ],
          [
           166.91189575195312
          ],
          [
           168.17059326171875
          ],
          [
           168.08140563964844
          ],
          [
           167.04075622558594
          ],
          [
           165.96044921875
          ],
          [
           164.31520080566406
          ],
          [
           172.02601623535156
          ],
          [
           171.95663452148438
          ],
          [
           170.24200439453125
          ],
          [
           172.01609802246094
          ],
          [
           172.20440673828125
          ],
          [
           171.27146911621094
          ],
          [
           170.77525329589844
          ],
          [
           170.77525329589844
          ],
          [
           171.3905792236328
          ],
          [
           173.73280334472656
          ],
          [
           173.8419952392578
          ],
          [
           172.8892059326172
          ],
          [
           170.26907348632812
          ],
          [
           170.5469512939453
          ],
          [
           171.6883087158203
          ],
          [
           174.1099395751953
          ],
          [
           175.9658660888672
          ],
          [
           175.91627502441406
          ],
          [
           178.73486328125
          ],
          [
           179.58839416503906
          ],
          [
           178.2287139892578
          ],
          [
           177.86151123046875
          ],
          [
           176.4819793701172
          ],
          [
           179.21127319335938
          ],
          [
           179.59835815429688
          ],
          [
           182.40704345703125
          ],
          [
           181.93064880371094
          ],
          [
           182.5658416748047
          ],
          [
           184.6103515625
          ],
          [
           183.52853393554688
          ],
          [
           183.61785888671875
          ],
          [
           182.57577514648438
          ],
          [
           185.59288024902344
          ],
          [
           185.27528381347656
          ],
          [
           183.8759002685547
          ],
          [
           186.6448974609375
          ],
          [
           187.82595825195312
          ],
          [
           188.16339111328125
          ],
          [
           192.5104522705078
          ],
          [
           191.01182556152344
          ],
          [
           189.89031982421875
          ],
          [
           190.36668395996094
          ],
          [
           189.24517822265625
          ],
          [
           187.19078063964844
          ],
          [
           186.6647491455078
          ],
          [
           188.34205627441406
          ],
          [
           189.1062469482422
          ],
          [
           189.255126953125
          ],
          [
           192.5302734375
          ],
          [
           192.27224731445312
          ],
          [
           193.6319580078125
          ],
          [
           191.67677307128906
          ],
          [
           190.4957275390625
          ],
          [
           191.2996063232422
          ],
          [
           192.16307067871094
          ],
          [
           193.03646850585938
          ],
          [
           191.7660675048828
          ],
          [
           194.3564453125
          ],
          [
           194.97178649902344
          ],
          [
           194.13809204101562
          ],
          [
           191.1309051513672
          ],
          [
           189.73150634765625
          ],
          [
           180.62060546875
          ],
          [
           177.50421142578125
          ],
          [
           178.44705200195312
          ],
          [
           176.84918212890625
          ],
          [
           176.63082885742188
          ],
          [
           176.6904754638672
          ],
          [
           178.3501434326172
          ],
          [
           176.35255432128906
          ],
          [
           175.47801208496094
          ],
          [
           172.92391967773438
          ],
          [
           173.410888671875
          ],
          [
           174.7525177001953
          ],
          [
           176.1339111328125
          ],
          [
           179.9998779296875
          ],
          [
           175.2891845703125
          ],
          [
           177.50540161132812
          ],
          [
           179.07562255859375
          ],
          [
           182.9813232421875
          ],
          [
           186.48948669433594
          ],
          [
           186.70814514160156
          ],
          [
           188.28829956054688
          ],
          [
           188.5268096923828
          ],
          [
           181.77880859375
          ],
          [
           176.46188354492188
          ],
          [
           177.0780487060547
          ],
          [
           178.25074768066406
          ],
          [
           175.20968627929688
          ],
          [
           173.13259887695312
          ],
          [
           174.65316772460938
          ],
          [
           173.92764282226562
          ],
          [
           176.86935424804688
          ],
          [
           177.96255493164062
          ],
          [
           174.40469360351562
          ],
          [
           172.85435485839844
          ],
          [
           173.70901489257812
          ],
          [
           174.9910430908203
          ],
          [
           170.89651489257812
          ],
          [
           169.37596130371094
          ],
          [
           169.63436889648438
          ],
          [
           170.15115356445312
          ],
          [
           172.6754608154297
          ],
          [
           171.33380126953125
          ],
          [
           172.5860137939453
          ],
          [
           173.82827758789062
          ],
          [
           176.39231872558594
          ],
          [
           177.883056640625
          ],
          [
           177.28675842285156
          ],
          [
           178.6880340576172
          ],
          [
           179.5924072265625
          ],
          [
           177.74391174316406
          ],
          [
           177.61473083496094
          ],
          [
           176.05442810058594
          ],
          [
           174.7525177001953
          ],
          [
           174.37489318847656
          ],
          [
           171.8108367919922
          ],
          [
           171.9300994873047
          ],
          [
           172.36737060546875
          ],
          [
           170.04185485839844
          ],
          [
           165.85789489746094
          ],
          [
           167.17965698242188
          ],
          [
           169.23684692382812
          ],
          [
           169.71388244628906
          ],
          [
           172.89407348632812
          ],
          [
           176.47183227539062
          ],
          [
           175.55752563476562
          ],
          [
           178.12156677246094
          ],
          [
           180.69554138183594
          ],
          [
           181.7589111328125
          ],
          [
           181.28189086914062
          ],
          [
           185.49127197265625
          ],
          [
           183.89907836914062
          ],
          [
           186.52621459960938
          ],
          [
           187.09341430664062
          ],
          [
           188.78515625
          ],
          [
           188.76524353027344
          ],
          [
           190.5166473388672
          ],
          [
           189.7106170654297
          ],
          [
           190.37733459472656
          ],
          [
           189.0438690185547
          ],
          [
           188.86474609375
          ],
          [
           189.47177124023438
          ],
          [
           188.44679260253906
          ],
          [
           189.02395629882812
          ],
          [
           190.3076934814453
          ],
          [
           188.50650024414062
          ],
          [
           192.47705078125
          ],
          [
           191.38243103027344
          ],
          [
           193.3229217529297
          ],
          [
           194.75588989257812
          ],
          [
           192.2382049560547
          ],
          [
           193.76077270507812
          ],
          [
           196.9949188232422
          ],
          [
           197.14418029785156
          ],
          [
           196.60682678222656
          ],
          [
           194.93499755859375
          ],
          [
           195.97988891601562
          ],
          [
           193.88018798828125
          ],
          [
           193.73089599609375
          ],
          [
           192.65618896484375
          ],
          [
           192.10885620117188
          ],
          [
           192.20835876464844
          ],
          [
           192.6362762451172
          ],
          [
           191.5913848876953
          ],
          [
           184.73497009277344
          ],
          [
           183.3517608642578
          ],
          [
           181.02316284179688
          ],
          [
           180.2967071533203
          ],
          [
           184.65536499023438
          ],
          [
           184.23741149902344
          ],
          [
           185.28228759765625
          ],
          [
           184.6852264404297
          ],
          [
           185.01361083984375
          ],
          [
           182.73477172851562
          ],
          [
           181.78941345214844
          ],
          [
           187.7104034423828
          ],
          [
           190.62611389160156
          ],
          [
           192.9447479248047
          ],
          [
           194.2284698486328
          ],
          [
           193.55177307128906
          ],
          [
           193.223388671875
          ],
          [
           191.48191833496094
          ],
          [
           190.79527282714844
          ],
          [
           187.12327575683594
          ],
          [
           183.5010223388672
          ],
          [
           185.94903564453125
          ],
          [
           184.94395446777344
          ],
          [
           186.7650146484375
          ],
          [
           188.37713623046875
          ],
          [
           188.48660278320312
          ],
          [
           187.40191650390625
          ],
          [
           188.1691436767578
          ],
          [
           186.47525024414062
          ],
          [
           184.37286376953125
          ],
          [
           183.48606872558594
          ],
          [
           183.19712829589844
          ],
          [
           181.6527099609375
          ],
          [
           180.90541076660156
          ],
          [
           181.66268920898438
          ],
          [
           183.70526123046875
          ],
          [
           181.86195373535156
          ],
          [
           180.50686645507812
          ],
          [
           181.97157287597656
          ],
          [
           180.76593017578125
          ],
          [
           180.0983428955078
          ],
          [
           179.01226806640625
          ],
          [
           174.4687042236328
          ],
          [
           169.5066680908203
          ],
          [
           168.51025390625
          ],
          [
           168.3907012939453
          ],
          [
           170.11447143554688
          ],
          [
           172.12718200683594
          ],
          [
           172.60543823242188
          ],
          [
           170.51303100585938
          ],
          [
           172.3762664794922
          ],
          [
           171.99765014648438
          ],
          [
           173.09368896484375
          ],
          [
           175.4451904296875
          ],
          [
           178.02581787109375
          ],
          [
           170.7521514892578
          ],
          [
           171.6588592529297
          ],
          [
           170.23403930664062
          ],
          [
           169.09814453125
          ],
          [
           172.68515014648438
          ],
          [
           170.86175537109375
          ],
          [
           169.4169921875
          ],
          [
           168.2312774658203
          ],
          [
           169.03834533691406
          ],
          [
           168.21136474609375
          ],
          [
           168.96859741210938
          ],
          [
           167.84268188476562
          ],
          [
           169.0582733154297
          ],
          [
           167.1750946044922
          ],
          [
           174.40892028808594
          ],
          [
           175.91348266601562
          ],
          [
           172.06739807128906
          ],
          [
           168.7693328857422
          ],
          [
           167.39430236816406
          ],
          [
           166.437744140625
          ],
          [
           164.40512084960938
          ],
          [
           165.24208068847656
          ],
          [
           166.2982635498047
          ],
          [
           168.41062927246094
          ],
          [
           169.27749633789062
          ],
          [
           168.6896209716797
          ],
          [
           172.8744659423828
          ],
          [
           169.7158966064453
          ],
          [
           168.6896209716797
          ],
          [
           172.4061737060547
          ],
          [
           182.71885681152344
          ],
          [
           181.0548858642578
          ],
          [
           181.7423858642578
          ],
          [
           182.0811767578125
          ],
          [
           183.90457153320312
          ],
          [
           182.63742065429688
          ],
          [
           185.8601531982422
          ],
          [
           187.00755310058594
          ],
          [
           189.2924041748047
          ],
          [
           189.41212463378906
          ],
          [
           189.4420623779297
          ],
          [
           190.6094207763672
          ],
          [
           191.91647338867188
          ],
          [
           190.46974182128906
          ],
          [
           186.45880126953125
          ],
          [
           189.5518035888672
          ],
          [
           189.56179809570312
          ],
          [
           189.86111450195312
          ],
          [
           190.85885620117188
          ],
          [
           191.8166961669922
          ],
          [
           193.59266662597656
          ],
          [
           193.91195678710938
          ],
          [
           195.42852783203125
          ],
          [
           194.04165649414062
          ],
          [
           196.4462432861328
          ],
          [
           192.68472290039062
          ],
          [
           206.68310546875
          ],
          [
           212.58978271484375
          ],
          [
           213.75714111328125
          ],
          [
           212.01107788085938
          ],
          [
           216.18165588378906
          ],
          [
           213.8070068359375
          ],
          [
           209.20741271972656
          ],
          [
           207.02235412597656
          ],
          [
           207.67086791992188
          ],
          [
           208.59878540039062
          ],
          [
           212.7693634033203
          ],
          [
           213.61746215820312
          ],
          [
           210.14527893066406
          ],
          [
           216.261474609375
          ],
          [
           219.77354431152344
          ],
          [
           221.0506591796875
          ],
          [
           225.82984924316406
          ],
          [
           227.30653381347656
          ],
          [
           228.16458129882812
          ],
          [
           232.4548797607422
          ],
          [
           227.05709838867188
          ],
          [
           230.0203857421875
          ],
          [
           233.87168884277344
          ],
          [
           234.29075622558594
          ],
          [
           228.3641357421875
          ],
          [
           223.67471313476562
          ],
          [
           223.80442810058594
          ],
          [
           223.45523071289062
          ],
          [
           224.5028533935547
          ],
          [
           218.04742431640625
          ],
          [
           216.99981689453125
          ],
          [
           217.46875
          ],
          [
           217.7481231689453
          ],
          [
           218.30685424804688
          ],
          [
           221.5794677734375
          ],
          [
           217.8678436279297
          ],
          [
           219.3644561767578
          ],
          [
           208.79833984375
          ],
          [
           206.76292419433594
          ],
          [
           209.34710693359375
          ],
          [
           212.8292236328125
          ],
          [
           215.7526397705078
          ],
          [
           217.2909393310547
          ],
          [
           221.02682495117188
          ],
          [
           221.47633361816406
          ],
          [
           224.47303771972656
          ],
          [
           225.80157470703125
          ],
          [
           225.64175415039062
          ],
          [
           226.2610626220703
          ],
          [
           226.15118408203125
          ],
          [
           224.2832489013672
          ],
          [
           226.5906982421875
          ],
          [
           226.93032836914062
          ],
          [
           227.77938842773438
          ],
          [
           226.2410888671875
          ],
          [
           229.53746032714844
          ],
          [
           228.7483367919922
          ],
          [
           222.52517700195312
          ],
          [
           220.6072998046875
          ],
          [
           222.13560485839844
          ],
          [
           220.57733154296875
          ],
          [
           220.66722106933594
          ],
          [
           219.86810302734375
          ],
          [
           222.41529846191406
          ],
          [
           222.52517700195312
          ],
          [
           222.25547790527344
          ],
          [
           216.082275390625
          ],
          [
           216.55174255371094
          ],
          [
           220.4474639892578
          ],
          [
           228.61846923828125
          ],
          [
           227.94920349121094
          ],
          [
           226.2211151123047
          ],
          [
           227.1201171875
          ],
          [
           226.1212158203125
          ],
          [
           227.26995849609375
          ],
          [
           227.53965759277344
          ],
          [
           232.7439422607422
          ],
          [
           225.96141052246094
          ],
          [
           226.53077697753906
          ],
          [
           225.42198181152344
          ],
          [
           226.55075073242188
          ],
          [
           221.4463653564453
          ],
          [
           225.52188110351562
          ],
          [
           229.28773498535156
          ],
          [
           228.7882843017578
          ],
          [
           227.2999267578125
          ],
          [
           231.04580688476562
          ],
          [
           233.59300231933594
          ],
          [
           231.5252685546875
          ],
          [
           231.89486694335938
          ],
          [
           234.74172973632812
          ],
          [
           236.22010803222656
          ],
          [
           235.60079956054688
          ],
          [
           230.5063934326172
          ],
          [
           230.31661987304688
          ],
          [
           231.1556854248047
          ],
          [
           233.14349365234375
          ],
          [
           233.41319274902344
          ],
          [
           229.8471221923828
          ],
          [
           225.66172790527344
          ],
          [
           222.66502380371094
          ],
          [
           221.76600646972656
          ],
          [
           223.2044219970703
          ],
          [
           222.47523498535156
          ],
          [
           227.22999572753906
          ],
          [
           226.9600067138672
          ],
          [
           224.22999572753906
          ],
          [
           224.22999572753906
          ],
          [
           225.1199951171875
          ],
          [
           228.22000122070312
          ],
          [
           225
          ],
          [
           228.02000427246094
          ],
          [
           228.27999877929688
          ],
          [
           229
          ],
          [
           228.52000427246094
          ],
          [
           229.8699951171875
          ],
          [
           232.8699951171875
          ],
          [
           235.05999755859375
          ],
          [
           234.92999267578125
          ],
          [
           237.3300018310547
          ],
          [
           239.58999633789062
          ],
          [
           242.64999389648438
          ],
          [
           243.00999450683594
          ],
          [
           243.0399932861328
          ],
          [
           242.83999633789062
          ],
          [
           246.75
          ],
          [
           247.77000427246094
          ],
          [
           246.49000549316406
          ],
          [
           247.9600067138672
          ],
          [
           248.1300048828125
          ],
          [
           251.0399932861328
          ],
          [
           253.47999572753906
          ],
          [
           248.0500030517578
          ],
          [
           249.7899932861328
          ],
          [
           254.49000549316406
          ],
          [
           255.27000427246094
          ],
          [
           258.20001220703125
          ],
          [
           259.0199890136719
          ],
          [
           255.58999633789062
          ],
          [
           252.1999969482422
          ]
         ]
        },
        {
         "mode": "lines",
         "name": "Forecast",
         "type": "scatter",
         "x": [
          "2024-12-31T00:00:00",
          "2025-01-01T00:00:00",
          "2025-01-02T00:00:00",
          "2025-01-03T00:00:00",
          "2025-01-06T00:00:00",
          "2025-01-07T00:00:00",
          "2025-01-08T00:00:00",
          "2025-01-09T00:00:00",
          "2025-01-10T00:00:00",
          "2025-01-13T00:00:00",
          "2025-01-14T00:00:00",
          "2025-01-15T00:00:00",
          "2025-01-16T00:00:00",
          "2025-01-17T00:00:00",
          "2025-01-20T00:00:00",
          "2025-01-21T00:00:00",
          "2025-01-22T00:00:00",
          "2025-01-23T00:00:00",
          "2025-01-24T00:00:00",
          "2025-01-27T00:00:00",
          "2025-01-28T00:00:00",
          "2025-01-29T00:00:00",
          "2025-01-30T00:00:00",
          "2025-01-31T00:00:00",
          "2025-02-03T00:00:00",
          "2025-02-04T00:00:00",
          "2025-02-05T00:00:00",
          "2025-02-06T00:00:00",
          "2025-02-07T00:00:00",
          "2025-02-10T00:00:00"
         ],
         "y": [
          228.12102780053462,
          227.9831899801956,
          227.91162145395242,
          227.96358530821428,
          228.00993693235893,
          228.00714185043114,
          228.001951783519,
          228.00038282927986,
          228.00181182540024,
          228.00258031922178,
          228.00248400865462,
          228.00233915813342,
          228.00231594423354,
          228.00235022788414,
          228.00236384199417,
          228.00236058806212,
          228.00235711903142,
          228.00235691638517,
          228.00235770898578,
          228.002357950917,
          228.00235785216913,
          228.00235777597854,
          228.00235777841283,
          228.00235779641784,
          228.00235780048115,
          228.00235779775127,
          228.00235779617296,
          228.00235779637427,
          228.00235779677575,
          228.00235779683555
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Stock Price Forecast"
        },
        "xaxis": {
         "title": {
          "text": "Date"
         }
        },
        "yaxis": {
         "title": {
          "text": "Price"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "\n",
    "# Generate forecast_dates\n",
    "last_date = data.index[-1]  # Get the last date from the dataset\n",
    "forecast_dates = pd.date_range(start=last_date, periods=30 + 1, freq='B')[1:]  # Next 30 business days\n",
    "\n",
    "# Plot the data\n",
    "fig = go.Figure()\n",
    "fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Actual'))\n",
    "fig.add_trace(go.Scatter(x=forecast_dates, y=forecast, mode='lines', name='Forecast'))\n",
    "fig.update_layout(title=\"Stock Price Forecast\", xaxis_title=\"Date\", yaxis_title=\"Price\")\n",
    "fig.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "\n",
      "1 Failed download:\n",
      "['AAPL']: ReadTimeout(ReadTimeoutError(\"HTTPSConnectionPool(host='query2.finance.yahoo.com', port=443): Read timed out. (read timeout=10)\"))\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "\n",
      "1 Failed download:\n",
      "['AAPL']: ReadTimeout(ReadTimeoutError(\"HTTPSConnectionPool(host='query2.finance.yahoo.com', port=443): Read timed out. (read timeout=10)\"))\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "\n",
      "1 Failed download:\n",
      "['AAPL']: ReadTimeout(ReadTimeoutError(\"HTTPSConnectionPool(host='query2.finance.yahoo.com', port=443): Read timed out. (read timeout=10)\"))\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "\n",
      "1 Failed download:\n",
      "['AAPL']: ReadTimeout(ReadTimeoutError(\"HTTPSConnectionPool(host='query2.finance.yahoo.com', port=443): Read timed out. (read timeout=10)\"))\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "\n",
      "1 Failed download:\n",
      "['AAPL']: ReadTimeout(ReadTimeoutError(\"HTTPSConnectionPool(host='query2.finance.yahoo.com', port=443): Read timed out. (read timeout=10)\"))\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "Run time of job \"fetch_realtime_data (trigger: interval[0:01:00], next run at: 2025-01-03 09:01:04 CET)\" was missed by 0:00:02.091277\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "[*********************100%***********************]  1 of 1 completed\n"
     ]
    }
   ],
   "source": [
    "from apscheduler.schedulers.background import BackgroundScheduler\n",
    "\n",
    "def fetch_realtime_data():\n",
    "    latest_data = yf.download(ticker, period=\"1d\", interval=\"1m\")\n",
    "    # Update your database or dashboard with new data\n",
    "\n",
    "scheduler = BackgroundScheduler()\n",
    "scheduler.add_job(fetch_realtime_data, 'interval', minutes=1)\n",
    "scheduler.start()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-02 15:58:55.758 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-02 15:58:55.821 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Users/titiksha/dev/cla_christmas_break/.venv/lib/python3.10/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-01-02 15:58:55.821 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-02 15:58:55.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-02 15:58:55.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-02 15:58:55.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-02 15:58:55.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-02 15:58:55.823 Session state does not function when running a script without `streamlit run`\n",
      "2025-01-02 15:58:55.823 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-02 15:58:55.823 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "[*********************100%***********************]  1 of 1 completed\n",
      "2025-01-02 15:58:58.185 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-02 15:58:58.186 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"Stock Market Analysis and Forecasting\")\n",
    "ticker_input = st.text_input(\"Enter Stock Ticker\", \"AAPL\")\n",
    "\n",
    "if ticker_input:\n",
    "    stock_data = yf.download(ticker_input, start=\"2015-01-01\")\n",
    "    st.line_chart(stock_data['Close'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

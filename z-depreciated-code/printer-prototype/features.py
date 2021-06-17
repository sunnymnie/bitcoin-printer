from ta.volatility import *
from ta.volume import *
from ta.trend import *
from ta.momentum import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '..')
import useful_functions as uf


def get_moving_average(close, span):
    """returns the moving average"""
    i = SMAIndicator(close, window=span)
    return i.sma_indicator()


def add_all_features(df):
    """adds all the features for model_minute_tpsl_1.0, returns the df"""
    df.reset_index(drop=True, inplace=True)
    df = target_indicators(df)
    df = momentum_indicators(df)
    df = trend_indicators(df)
    df = volatility_indicators(df)
    df = volume_indicators(df)
    df = special_indicators(df)
    return df


def target_indicators(df):
    """returns target indicators"""
    high, low, close, volume = convert_df_to_features(df, True)
    i = NegativeVolumeIndexIndicator(close, volume)
    nvi_o_close = pd.Series(
        list(map(lambda n, c: n / c, i.negative_volume_index(), close)))
    nvi = uf.get_rate(uf.get_moving_average(nvi_o_close, 50))
    df["nvi"] = uf.classify(nvi, 0.)

    i = BollingerBands(close, window=100, window_dev=2)
    df["bb"] = i.bollinger_pband()
    df["bb"] = uf.classify(list(map(lambda x: -x, df.bb)), -0.2)
    return df


def momentum_indicators(df):
    """returns the momentum indicators"""
    p = "mom_"
    high, low, close = convert_df_to_features(df, False)
    # AO
    i = AwesomeOscillatorIndicator(high, low, 10, 70)
    df[p + "ao_10_log"] = list(map(lambda x: uf.log_abs(x,
                               zeros=True), i.awesome_oscillator()))
    # PPO
    i = PercentagePriceOscillator(close, 40, 20, 10)
    df[p + "ppo_10_signal_log"] = list(
        map(lambda x: uf.log_abs(x * 1000), i.ppo_signal()))
    i = PercentagePriceOscillator(close, 120, 60, 30)
    df[p + "ppo_30_hist"] = i.ppo_hist()
    # ROC
    i = ROCIndicator(close, 50)
    df[p + "roc_50_log"] = list(map(lambda x: uf.log_abs(x *
                                100, zeros=True), i.roc()))
    # RSI
    i = RSIIndicator(close, 30)
    df[p + "rsi_30"] = i.rsi()
    # SR
    i = StochasticOscillator(close, high, low, 54, 9)
    df[p + "sr_9_signal"] = i.stoch_signal()
    # SRSI
    i = StochRSIIndicator(close, 90, 15, 15)
    df[p + "srsi_15_k"] = i.stochrsi_k()
    i = StochRSIIndicator(close, 180, 30, 30)
    df[p + "srsi_30"] = i.stochrsi()
    i = StochRSIIndicator(close, 60, 10, 10)
    df[p + "srsi_10_d"] = i.stochrsi()
    # TSI
    i = TSIIndicator(close, 40, 20)
    df[p + "tsi_20_log"] = list(map(lambda x: uf.log_abs(x *
                                100, zeros=True), i.tsi()))
    # WR
    i = WilliamsRIndicator(high, low, close, 50)
    df[p + "wr_50"] = i.williams_r()
    return df


def trend_indicators(df):
    """returns the trend indicators"""
    p = "trend_"
    high, low, close = convert_df_to_features(df, False)

    # ADX
    i = ADXIndicator(high, low, close, window=40)
    df[p + "adx_40_neg"] = i.adx_neg()
    # ARN
    i = AroonIndicator(close, window=50)
    df[p + "arn_50"] = i.aroon_indicator()
    # CCI
    i = CCIIndicator(high, low, close, window=70)
    df[p + "cci_70"] = i.cci()
    # DPO
    i = DPOIndicator(close, window=100)
    df[p +
        "dpo_100_log"] = list(map(lambda x: uf.log_abs(x, zeros=True), i.dpo()))
    # KST
    i = KSTIndicator(close)
    df[p + "kst_sig_log"] = list(map(lambda x: uf.log_abs(x,
                                 zeros=True), i.kst_sig()))
    # MACD
    i = MACD(close, 12, 16, 34)
    df[p + "macd_12_signal_log"] = list(
        map(lambda x: uf.log_abs(x, zeros=True), i.macd_signal()))
    # SMA
    i = SMAIndicator(close, window=50)  # 50

    sma_50_rate = uf.get_rate(i.sma_indicator())
    df[p + "sma_50_rate_log"] = list(
        map(lambda x: uf.log_abs(x, zeros=True), sma_50_rate))

    sma_50_diff = list(map(lambda s, c: uf.none_subtraction(
        s, c), i.sma_indicator(), close))
    df[p + "sma_50_diff_log"] = list(
        map(lambda x: uf.log_abs(x, zeros=True), sma_50_diff))

    i = SMAIndicator(close, window=200)

    sma_200_diff = list(
        map(lambda s, c: uf.none_subtraction(s, c), i.sma_indicator(), close))
    sma_200_diff_o_close = list(
        map(lambda s, c: s / c, sma_200_diff, close))
    df[p + "sma_200_diff_o_close_log"] = list(
        map(lambda x: uf.log_abs(x * 100, zeros=True), sma_200_diff_o_close))
    # STC
    i = STCIndicator(close, 100, 200, 50)
    df[p + "stc_50_2"] = i.stc()
    # TRIX
    i = TRIXIndicator(close, window=20)
    df[p + "trix_20_log"] = list(map(lambda x: uf.log_abs(x * 1000), i.trix()))
    # VI
    i = VortexIndicator(high, low, close, window=50)
    df[p + "vi_50_amp"] = list(map(lambda x: uf.log_abs(x *
                               1000, zeros=True), i.vortex_indicator_diff()))

    return df


def volatility_indicators(df):
    """returns the volatility indicators"""
    p = "volatility_"
    high, low, close = convert_df_to_features(df, False)

    # ATR
    atr = AverageTrueRange(high, low, close, 14)
    df[p + "atr_14"] = atr.average_true_range()
    df[p + "atr_o_close"] = list(map(lambda a,
                                 c: a / c, df[p + "atr_14"], close))
    # BB
    bb = BollingerBands(close, window=10, window_dev=2)
    df[p + "bb_wband_10"] = bb.bollinger_wband()

    bb = BollingerBands(close, window=100, window_dev=2)
    df[p + "bb_pband_100"] = bb.bollinger_pband()

    bb = BollingerBands(close, window=200, window_dev=2)
    df[p + "bb_wband_200"] = bb.bollinger_wband()

    bb = BollingerBands(close, window=20, window_dev=2)
    df[p + "bb_hband_o_close"] = list(map(lambda l,
                                      c: (l - c) / c, bb.bollinger_hband(), close))

    # DC
    dc = DonchianChannel(high, low, close, window=50)
    df[p + "dc_pband_50"] = dc.donchian_channel_pband()
    dc = DonchianChannel(high, low, close, window=10)
    df[p + "dc_wband_10"] = dc.donchian_channel_wband()
    # KC
    kc = KeltnerChannel(high, low, close, window=50)
    df[p + "pband_50"] = kc.keltner_channel_pband()
    kc = KeltnerChannel(high, low, close, window=20)
    df[p + "wband_20"] = kc.keltner_channel_wband()
    # UI
    ui = UlcerIndex(close, window=30)
    df[p + "ui_30"] = ui.ulcer_index()
    return df


def volume_indicators(df):
    """returns the volume indicators"""

    p = "volume_"
    high, low, close, volume = convert_df_to_features(df, True)

    # CMF
    cmf = ChaikinMoneyFlowIndicator(
        high, low, close, volume, window=50)
    df[p + "cmf_50"] = cmf.chaikin_money_flow()
    df[p + "cmf_50_rate_200"] = uf.get_rate(
        uf.get_moving_average(cmf.chaikin_money_flow(), 200))
    # EOM EMV
    eom = EaseOfMovementIndicator(high, low, volume, window=50)
    df[p + "eom_amplified"] = list(map(lambda x: uf.log_abs(x * 10),
                                   eom.sma_ease_of_movement()))
    # FI
    i = ForceIndexIndicator(close, volume, window=80)
    df[p +
        "fi_amplified"] = list(map(lambda x: uf.log_abs(x * 10), i.force_index()))
    # MFI
    i = MFIIndicator(high, low, close, volume, window=50)
    df[p + "mfi_50"] = i.money_flow_index()
    # NVI
    i = NegativeVolumeIndexIndicator(close, volume)
    nvi_o_close = pd.Series(
        list(map(lambda n, c: n / c, i.negative_volume_index(), close)))
    df[p + "nvi_o_close_rate_50"] = uf.get_rate(
        uf.get_moving_average(nvi_o_close, 50))
    return df


def special_indicators(df):
    """returns special indicators"""
    high, low, close, volume = convert_df_to_features(df, True)

    name = "rsi_"
    for w in [100, 1000]:
        i = RSIIndicator(close, w)
        df[name + str(w)] = i.rsi()
        df[name + "rate_" +
            str(w)] = uf.get_rate(uf.get_moving_average(df[name + str(w)], w))

    name = "arn_"
    for w in [100, 1000]:
        i = AroonIndicator(close, window=w)
        df[name + "down_" + str(w)] = i.aroon_down()
        df[name + str(w)] = i.aroon_indicator()
        df[name + "up_" + str(w)] = i.aroon_up()
        df[name + "rate_" +
            str(w)] = uf.get_rate(uf.get_moving_average(df[name + str(w)], w))
        df[name + "down_rate_" +
            str(w)] = uf.get_rate(uf.get_moving_average(df[name + "down_" + str(w)], w))
        df[name + "up_rate_" +
            str(w)] = uf.get_rate(uf.get_moving_average(df[name + "up_" + str(w)], w))

    name = "bb_"
    for w in [100, 1000]:
        bb = BollingerBands(close, window=w, window_dev=2)
        df[name + "pband_" + str(w)] = bb.bollinger_pband()
        # width band, try width/close
        df[name + "wband_" + str(w)] = bb.bollinger_wband()
        df[name + "pband_rate_" +
            str(w)] = uf.get_rate(uf.get_moving_average(df[name + "pband_" + str(w)], w))
        df[name + "wband_rate_" +
            str(w)] = uf.get_rate(uf.get_moving_average(df[name + "wband_" + str(w)], w))

    name = "fi_"
    for w in [100, 1000]:
        i = ForceIndexIndicator(close, volume, window=w)
        df[name + str(w)] = list(map(lambda x: uf.log_abs(x * 10),
                                     i.force_index()))
        df[name + "rate_" +
            str(w)] = uf.get_rate(uf.get_moving_average(df[name + str(w)], w))

    df.drop(["bb_pband_100"], axis=1, inplace=True)
    return df


def convert_df_to_features(df, volume=False):
    """converts df to high, low, close, and volume with .astype(float) so it
    works properly"""
    if volume:
        return df.high.astype(float), df.low.astype(float), df.close.astype(float), df.volume.astype(float)
    else:
        return df.high.astype(float), df.low.astype(float), df.close.astype(float)

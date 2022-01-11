import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df=pd.read_csv("fcc-forum-pageviews.csv",parse_dates=["date"],index_col="date")

#clean data
df= df[
    (df["value"] >= df["value"].quantile(0.025))&
    (df["value"] <= df["value"].quantile(0.095))]

def draw_line_plot():
    fig, ax =plt.subplot(figsize=(10,5))
    ax.plot(df.index,df['value'],'r',linewidth=1)

    ax.set_title('daily fcc page views')
    ax.set_xlable('Date')
    ax.set_ylable('page_views')

    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    df["month"]=df.index.month
    df["year"]=df.index.year
    df_bar=df.groupby(["year","month"])["value"].mean()
    df_bar=df_bar.unstack()

    fig=df_bar.plot.bar(legend= True, figsize=(10,5),ylabel="average page views",xlabel="years" ).figure
    plt.legends(['jan','feb','mar','april','may','june','july','aug','sep','oct','nov','dec'])

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
# Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

 
    # draw box plots
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")


    fig ,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,5))
    axes[0]=sns.boxplot(x=df_box["year"],y=df_box["value"],ax=axes[0])
    axes[1]=sns.boxplot(x=df_box["month"],y=df_box["value"],ax=axes[1])
    axes[0].set_title("year-wise")
    axes[0].set_xlabel("year")
    axes[0].set_ylabel("page views")

    axes[1].set_title("month-wise")
    axes[1].set_xlabel("month")
    axes[1].set_ylabel("page views")

    fig.savefig('box_plot.png')
    return fig

















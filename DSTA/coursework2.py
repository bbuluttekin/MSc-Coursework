import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import seaborn as sns

import numpy as np


# read file
# please use pdf file as a documentation
df = pd.read_csv("heart.csv")
df.head()

selected_dims = ["age", "chol", "trestbps", "target"]

df_selected = df[selected_dims]
df_selected[["target"]] = ["Hearth Desease" if i ==
                           1 else "Normal" for i in df["target"]]
df_selected.dtypes

sns.pairplot(df_selected, hue="target")

y = df["target"]

pca = PCA(n_components=3)
df_reduced = pca.fit_transform(df[df.columns[:-1]])
pca.explained_variance_ratio_


def plot_3d(dataframe, x_label, y_label, z_label, target_label, title):
    labelTups = [("Normal", 0), ("Hearth Desease", 1)]
    fig = plt.figure(1, figsize=(8, 6))
    ax = Axes3D(fig, elev=-150, azim=110)
    ax.scatter(dataframe[x_label], dataframe[y_label], dataframe[z_label], c=dataframe[target_label],
               cmap=plt.cm.Set1, edgecolor='k', s=40)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.w_xaxis.set_ticklabels([])
    ax.set_ylabel(y_label)
    ax.w_yaxis.set_ticklabels([])
    ax.set_zlabel(z_label)
    ax.w_zaxis.set_ticklabels([])

    sc = ax.scatter(dataframe[x_label], dataframe[y_label], dataframe[z_label],
                    c=dataframe[target_label], cmap="Spectral", edgecolor='k')

    colors = [sc.cmap(sc.norm(i)) for i in [1, 0]]
    custom_lines = [plt.Line2D([], [], ls="", marker='.',
                               mec='k', mfc=c, mew=.1, ms=20) for c in colors]
    lgd = ax.legend(custom_lines, [lt[0] for lt in labelTups],
                    loc='center left', bbox_to_anchor=(1.0, .5))
    #fig.savefig('{}-{}-{}-{}.png'.format(title, x_label, y_label, z_label), dpi=fig.dpi, bbox_extra_artists=(lgd), bbox_inches='tight')
    #files.download('{}-{}-{}-{}.png'.format(title, x_label, y_label, z_label))
    plt.show()


plot_3d(df, "age", "chol", "trestbps", "target",
        "Heart Desease clustering by 3 dimensions")

labelTups = [("Normal", 0), ("Hearth Desease", 1)]
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(df_reduced[:, 0], df_reduced[:, 1], df_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("PCA with 3 components")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

sc = ax.scatter(df_reduced[:, 0], df_reduced[:, 1],
                df_reduced[:, 2], c=y, cmap="Spectral", edgecolor='k')

colors = [sc.cmap(sc.norm(i)) for i in [1, 0]]
custom_lines = [plt.Line2D([], [], ls="", marker='.',
                           mec='k', mfc=c, mew=.1, ms=20) for c in colors]
ax.legend(custom_lines, [lt[0] for lt in labelTups],
          loc='center left', bbox_to_anchor=(1.0, .5))


# searched pca components
pca_search = PCA()
pca_search.fit_transform(df[df.columns[:-1]])
cum_sum = np.cumsum(pca_search.explained_variance_ratio_)
confidence_degree = np.argmax(cum_sum >= 0.95) + 1

print(confidence_degree)

plt.plot(list(range(1, len(cum_sum) + 1)), cum_sum)
plt.xlabel("Number of components")
plt.ylabel("Explained variance")

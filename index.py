import pandas as pd
import plotly.express as px

df = pd.read_csv('Pokemon.csv')

# 1. Distribution des Types de Pokémon
type_counts = df['Type 1'].value_counts().reset_index()
type_counts.columns = ['Type', 'Nombre']
fig1 = px.bar(type_counts, x='Type', y='Nombre',
              title='Distribution des Types de Pokémon (Type 1)',
              color='Type')
fig1.show()

# 2. Top 15 Pokémon par Total de Stats
top15 = df.nlargest(15, 'Total')
fig2 = px.bar(top15, x='Name', y='Total',
              title='Top 15 Pokémon par Total de Stats',
              color='Total', color_continuous_scale='Viridis',
              hover_data=['Type 1', 'Type 2', 'Generation'])
fig2.show()

# 3. Attack vs Defense (coloré par Type)
fig3 = px.scatter(df, x='Attack', y='Defense',
                  hover_name='Name', color='Type 1',
                  size='Total', title='Attack vs Defense par Type',
                  hover_data=['HP', 'Speed', 'Generation'])
fig3.show()

# 4. Stats moyennes par Génération
stats_cols = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
stats_gen = df.groupby('Generation')[stats_cols].mean().reset_index()
fig4 = px.line(stats_gen, x='Generation', y=stats_cols,
               title='Stats Moyennes par Génération',
               labels={'value': 'Valeur Moyenne', 'variable': 'Stat'},
               markers=True)
fig4.show()

# 5. Légendaires vs Non-Légendaires
fig5 = px.box(df, x='Legendary', y='Total', color='Legendary',
              title='Distribution du Total - Légendaires vs Non-Légendaires',
              points='outliers')
fig5.show()

# 7. Heatmap de corrélation entre les stats
corr = df[stats_cols + ['Total']].corr()
fig7 = px.imshow(corr, text_auto='.2f',
                 title='Corrélation entre les Stats',
                 color_continuous_scale='RdBu_r')
fig7.show()

# 8. Répartition Légendaires par Type
legendary_df = df[df['Legendary'] == True]
leg_type = legendary_df['Type 1'].value_counts().reset_index()
leg_type.columns = ['Type', 'Nombre']
fig8 = px.pie(leg_type, values='Nombre', names='Type',
              title='Répartition des Pokémon Légendaires par Type')
fig8.show()
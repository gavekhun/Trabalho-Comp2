import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos dados e limpeza dos dados
netflix_df = pd.read_csv('netflix_titles.csv')
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce')
netflix_df['year_added'] = netflix_df['date_added'].dt.year
netflix_df['country'] = netflix_df['country'].fillna('Desconhecido')
netflix_df['rating'] = netflix_df['rating'].fillna('Desconhecido')
netflix_df['duration'] = netflix_df['duration'].fillna('0')

# Visualização inicial
print("\nVisualização inicial:")
print(netflix_df.head())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(netflix_df.describe(include='all'))
print("\nValores ausentes:")
print(netflix_df.isnull().sum())
print("\nInformações do DataFrame:")
netflix_df.info()

# Distribuição por tipo
netflix_df['type'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'], title='Distribuição de Tipo de Conteúdo')
plt.xlabel('Tipo')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()

# Distribuição de lançamentos por ano
netflix_df['release_year'].value_counts().sort_index().plot(kind='bar', figsize=(10,4), color='orange', title='Distribuição por Ano de Lançamento')
plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()

# Top 10 países com mais títulos
country_data = netflix_df['country'].str.split(', ').explode().value_counts().head(10)
country_data.plot(kind='bar', color='green', title='Top 10 Países de Produção')
plt.xlabel('País')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()

# Adições ao catálogo por ano
netflix_df['year_added'].value_counts().sort_index().plot(kind='bar', color='purple', title='Ano de Adição ao Catálogo')
plt.xlabel('Ano de Adição')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()

# Gêneros mais frequentes
genres = netflix_df['listed_in'].str.split(', ').explode().value_counts().head(10)
genres.plot(kind='bar', color='teal', title='Gêneros Mais Frequentes')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.show()

# Correlação entre ano de lançamento e ano de adição
corr_netflix_df = netflix_df[['release_year', 'year_added']].dropna()
plt.scatter(corr_netflix_df['release_year'], corr_netflix_df['year_added'], alpha=0.5, color='gray')
plt.title('Ano de Lançamento vs Ano de Adição')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Ano de Adição')
plt.tight_layout()
plt.show()

# Distribuição da duração dos conteúdos
plt.figure(figsize=(8,4))
netflix_df['duration'].value_counts().head(20).plot(kind='bar', color='coral')
plt.title('Top Durações de Conteúdo')
plt.xlabel('Duração')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()


import streamlit as st
import pandas as pd
import plotly.express as px

class NetflixAnalyzer:
    def __init__(self, data_path):
        self.data = self._load_and_clean(data_path)

    def _load_and_clean(self, path):
        df = pd.read_csv(path)
        df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
        df['year_added'] = df['date_added'].dt.year
        df['month_added'] = df['date_added'].dt.month
        df['country'] = df['country'].fillna('Desconhecido')
        df['listed_in'] = df['listed_in'].fillna('Desconhecido')
        df['rating'] = df['rating'].fillna('Desconhecido')
        df['duration'] = df['duration'].fillna('Desconhecido')
        df['duration_minutes'] = df['duration'].str.extract(r'(\d+)').astype('float')
        df['director'] = df['director'].fillna('Desconhecido')
        return df

    def get_filtered_data(self, content_type, year_range, countries=None):
        filtered = self.data[
            (self.data['release_year'] >= year_range[0]) &
            (self.data['release_year'] <= year_range[1])
        ]
        if content_type != 'Todos':
            filtered = filtered[filtered['type'] == content_type]
        if countries and 'Todos' not in countries:
            filtered = filtered[filtered['country'].str.contains('|'.join(countries))]
        return filtered

class NetflixDashboard:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def render_sidebar(self):
        st.sidebar.header('🎛️ Filtros')
        content_type = st.sidebar.selectbox('Tipo de Conteúdo', ['Todos', 'Movie', 'TV Show'])

        min_year = int(self.analyzer.data['release_year'].min())
        max_year = int(self.analyzer.data['release_year'].max())
        year_range = st.sidebar.slider('Ano de Lançamento', min_year, max_year, (2010, max_year))

        all_countries = sorted(set(
            country for sublist in self.analyzer.data['country'].str.split(', ').dropna()
            for country in sublist
        ))
        selected_countries = st.sidebar.multiselect('País(es)', ['Todos'] + all_countries, default=['Todos'])

        return content_type, year_range, selected_countries

    def render_main_content(self, filtered_data):
        st.title('📺 Netflix - Análise Exploratória de Dados')

        col1, col2, col3 = st.columns(3)
        col1.metric("Total", len(filtered_data))
        col2.metric("Filmes", len(filtered_data[filtered_data['type'] == 'Movie']))
        col3.metric("Séries", len(filtered_data[filtered_data['type'] == 'TV Show']))

        st.subheader('📈 Tendência de Adições por Ano')
        yearly = filtered_data['year_added'].value_counts().sort_index()
        yearly_df = pd.DataFrame({'Ano': yearly.index, 'Títulos Adicionados': yearly.values})
        fig = px.bar(yearly_df, x='Ano', y='Títulos Adicionados', labels={'Ano': 'Ano', 'Títulos Adicionados': 'Quantidade'})
        st.plotly_chart(fig)

        st.subheader('🆚 Comparativo Movie x TV Show por Ano')
        comparison = filtered_data.groupby(['year_added', 'type']).size().reset_index(name='count')
        fig = px.bar(comparison, x='year_added', y='count', color='type', barmode='group',
                     labels={'year_added': 'Ano', 'count': 'Quantidade'})
        st.plotly_chart(fig)

        st.subheader('🌍 Top 10 Países de Produção')
        countries = filtered_data['country'].str.split(', ').explode().value_counts().head(10)
        contries_df = pd.DataFrame({'País': countries.index, 'Número de Títulos': countries.values})
        fig = px.bar(contries_df, x='País', y='Número de Títulos')
        st.plotly_chart(fig)

        st.subheader('🎭 Principais Gêneros')
        genres = filtered_data['listed_in'].str.split(', ').explode().value_counts().head(10)
        genres_df = pd.DataFrame({'Gênero': genres.index, 'Frequência': genres.values})
        fig = px.bar(genres_df, x='Gênero', y='Frequência')
        st.plotly_chart(fig)

        st.subheader('🧑‍💼 Classificação Etária')
        ratings = filtered_data['rating'].value_counts().head(10)
        fig = px.pie(ratings, names=ratings.index, values=ratings.values, hole=0.4)
        st.plotly_chart(fig)

        st.subheader('🎬 Top 10 Diretores')
        directors = filtered_data['director'].str.split(', ').explode().value_counts().head(10)
        directors_df = pd.DataFrame({'Diretor': directors.index, 'Número de Títulos': directors.values})
        fig = px.bar(directors_df, x='Diretor', y='Número de Títulos')
        st.plotly_chart(fig)

        st.subheader('⏱️ Duração de Filmes (min)')
        if 'Movie' in filtered_data['type'].unique():
            movie_data = filtered_data[filtered_data['type'] == 'Movie']
            fig = px.histogram(movie_data, x='duration_minutes', nbins=30,
                               labels={'duration_minutes': 'Duração (min)'})
            st.plotly_chart(fig)

        st.subheader('📅 Correlação entre Ano de Lançamento e Adição')
        year_corr = filtered_data[['release_year', 'year_added']].dropna()
        fig = px.density_heatmap(
            year_corr,
            x='release_year',
            y='year_added',
            nbinsx=20,
            nbinsy=20,
            color_continuous_scale='Viridis',
            labels={'release_year': 'Ano de Lançamento', 'year_added': 'Ano Adicionado'}
        )
        st.plotly_chart(fig)

        st.subheader('📄 Dados Brutos')
        st.dataframe(filtered_data)

if __name__ == '__main__':
    st.set_page_config(page_title="Netflix EDA", layout="wide")
    analyzer = NetflixAnalyzer('netflix_titles.csv')
    dashboard = NetflixDashboard(analyzer)

    filters = dashboard.render_sidebar()
    filtered_data = analyzer.get_filtered_data(*filters)
    dashboard.render_main_content(filtered_data)

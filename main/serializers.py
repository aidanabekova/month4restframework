from rest_framework import serializers
from .models import Movie, Genre, Rating


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = 'id text value'.split()


class MovieSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True)
    # ratings = RatingSerializer(many=True)
    ratings = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['id', 'name', 'genres', 'ratings', 'count_genres', 'rating']

    def get_ratings(self, movie):
        return RatingSerializer(movie.ratings.filter(movie=movie, value__gt=3), many=True).data

        # rate = movie.ratings.filter(value__gt=3) #этот код и нижний работают абсолютно одинаково
        # rate = Rating.objects.filter(movie=movie, value__gt=3) #
        # data = RatingSerializer(rate, many=True).data      весь этот код можно прописать в одну строку
        # return data

    def get_genres(self, movie):
        return GenreSerializer(movie.genres.filter(is_active=True), many=True).data
        # filtered_genres = movie.genres.filter(is_active=True)
        # data = GenreSerializer(filtered_genres, many=True).data     весь этот код можно прописать в одну строку
        # return data


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        # fields = 'id name'.split()
        fields = ['id', 'name', 'description', 'duration', 'count_genres', 'rating']


from rest_framework.exceptions import ValidationError


class GenreCreatedSerializer(serializers.Serializer):
    name = serializers.CharField()
    is_active = serializers.BooleanField()

    def validate_name(self, name):
        movies = Genre.objects.filter(name=name)
        if movies:
            raise ValidationError('Genres already exists!')
        return name


class MovieCreateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=20)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField
    is_active = serializers.BooleanField(required=True)
    genres = serializers.ListField(child=serializers.IntegerField())
    created_genres = serializers.ListField(child=GenreCreatedSerializer(), required=False)

    def validate_name(self, name):
        for i in name:
            if ord(i) >= 1040 and ord(i) <= 1103:  # проверка на русский язык
                raise ValidationError('Please use english only!')
        return name

    #
    # def validate_name(self, name):
    #     movies = Movie.objects.filter(name=name)  # тотечная валидация(ищет по имени)
    #     if movies:
    #         raise ValidationError('Movie already exists!')
    #     return name

    # def validate(self, attrs):
    #     name = attrs['name']
    #     movies = Movie.objects.filter(name=name)  # кастомная(ручная) валидация
    #     if movies:
    #         raise ValidationEr

#import spacy and the library
import spacy
nlp = spacy.load('en_core_web_md')

#planet hulk movie description - comparing description

hulk_desc = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

#function that will take an inputted description return the name of the movie with the most similar description
def sim_movie(description):

    #define an empty dictionary for the movies and sim as zero to compare the similarity scores
    movie_dict = {}
    sim = 0

    #open the movie document and split the movie titles and descriptions and store them in the dictionary with the titles as keys
    with open('movies.txt', 'r+', encoding = 'utf-8') as movie_desc:
        for line in movie_desc:
            line = line.strip('\n')
            line = line.split(' :')
            movie_dict[line[0]] = line[1]
    
    #iterate through the movie dictionary and using the value(movie description) compare it to the inputted description
    #take the value for similarity and if it is greater than the previous value for similarity it will be stored as sim and the movie name saved as movie_rec  
    for key, value in movie_dict.items():
        similarity = nlp(value).similarity(nlp(description))
        if float(similarity) > sim:
            sim = similarity
            movie_rec = key
        
    return(movie_rec)

#print the recommended movie title using the sim_movie function
print(f'Upon recent viewing of planet Hulk we recommend you try {sim_movie(hulk_desc)} next!')



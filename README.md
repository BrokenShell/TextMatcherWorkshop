# TextMatcher Workshop

### Tech Stack
- Logic: Python
- Web Framework: Flask
- Template Engine: Jinja
- Templates: HTML5
- Styling: CSS3
- Machine Learning: Scikit NearestNeighbors
- Text Processing: spaCy

## TextMatcher: Primary Interface
Machine learning model featuring natural language processing 
trained on arbitrary text for the purpose of classification of arbitrary 
text. The class creates a callable object for making predictions. The instance 
is trained at initialization and the callable object is reusable for the same 
training data. TextMatcher uses a combination of SpaCy, TfidfVectorizer 
and NearestNeighbors.

## Tokenizer: Helper Class
Creates a callable object for tokenizing input data based on the en_core_web_sm 
SpaCy library.

### Training Data: train_data.py
Archetype training data for the example.
- The Hero
- The Caregiver
- The Explorer
- The Rebel
- The Lover
- The Artist
- The Entertainer
- The Sage
- The Magician
- The Ruler

### Test Data: test_data.py
Dictionary of biographies, to be used for the example.
- King Arthur
- Romeo
- Stevie Nicks
- Vincent van Gogh
- Pablo Picasso
- Aleister Crowley
- Tori Amos
- Luke Skywalker
- Florence Nightingale
- Lewis and Clark

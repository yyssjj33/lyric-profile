# lyric-profile

give a singer's name and find if his or her lyric is positive or negative


## Example command
```
(venv) ➜  lyric-profile git:(master) ✗ python cli.py --name="eminem"   
eminem's song is negative

```

### notice
please run following code to download nltk dictionaries first.
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')

```
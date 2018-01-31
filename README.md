# raspberry

### Connect to Raspberry Pi

```
ssh pi@192.168.86.40
```

Check the installed Python versions on your Raspberry Pi:

`python --version` = 2.7.13
`python3 --version` = 3.5.3

Install the matching Python 3 version on your local machine via [pyenv](https://github.com/pyenv/pyenv) on macOS:

```
pyenv install -v 3.5.3
pyenv rehash
```

Note: I had to run `xcode-select --install` because of a `ZipImportError` error before I was able to install 3.5.3 ([see](https://github.com/pyenv/pyenv/issues/454)).

## Some terminal wisdom

Leave Python shell: `control` + `d`
Leave VIM shell: `esc` and `:wq`

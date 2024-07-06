# kalgory-py

[![CI](https://github.com/kalgory-com/kalgory-py/actions/workflows/ci.yaml/badge.svg)](https://github.com/kalgory-com/kalgory-py/actions/workflows/ci.yaml)
[![Maintainability](https://api.codeclimate.com/v1/badges/354248f7e34319db351e/maintainability)](https://codeclimate.com/github/kalgory-com/kalgory-py/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/354248f7e34319db351e/test_coverage)](https://codeclimate.com/github/kalgory-com/kalgory-py/test_coverage)

Python library for [kalgory](https://kalgory.com), a visualization and drag n' drop tool for algorithmic trader. 

## Installations

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install kalgory.

```bash
pip install kalgory
```

## Usage

```python
from kalgory.component import BaseBlock

class Block(BaseBlock):
    def handle(self, **kwargs) -> bytes:
        # You can write any data handling logic here as you want
        pass
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MPL-2.0](https://choosealicense.com/licenses/mpl-2.0/)

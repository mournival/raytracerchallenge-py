<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[![raytracerchallenge-py Behave Demo](https://github.com/mournival/raytracerchallenge-py/actions/workflows/behave.yml/badge.svg)](https://github.com/mournival/raytracerchallenge-py/actions/workflows/behave.yml)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mournival/raytracerchallenge-py">
    <img src="images/logo.png" alt="Logo" width="80" height="60">
  </a>

<h3 align="center">Kris Holvoet's Python Ray Tracer Challenge</h3>

  <p align="center">
     A Python implementation of a Ray Tracer as described in The Ray Tracer Challenge
    <br />
    <a href="https://github.com/mournival/raytracerchallenge-py"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mournival/raytracerchallenge-py">View Demo</a>
    ·
    <a href="https://github.com/mournival/raytracerchallenge-py/issues">Report Bug</a>
    ·
    <a href="https://github.com/mournival/raytracerchallenge-py/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project <a name="about-the-project"></a>

![Ray Tracer Challenge](images/logo.png)

This is a Python implementation of a Ray Tracer as described
in [The Ray Tracer Challenge](http://raytracerchallenge.com/). The principal objective is personal development (in
particular mine), with an emphasis on:

* Practicing the Python Behave (Gherkin) testing framework
* Improving my Python
* Practicing fairly pure aspects of TDD
* (and Finally) Revisiting topics from a favorite graduate CS graphics class

### Constraints

Do NOT change / rewrite any of the given tests. Some 'exceptions to the rule':

* From previous (other language) implementations, the book pushes for mutable data. I'm not a fan. I may ignore or
  rewrite a test if mutability is required.
* Previous implementations didn't use 'common' frameworks for the APP code (test frameworks, sure). I am going to use
  real frameworks, i.e., numpy for the matrices and vectors. I already know how to implement
  student level numerical methods and classes.
* If adding tests to doc my discovered bugs / 'Putting it all together' implementations, they will be identified as
  added and separated from the original tests. (Honored in the breach at this point, been adding new tests and files,
  added extra 'Then ... clauses for mutation testing')

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With <a name="built-with"></a>

- [![PyPI - Python Version][PyPi]][PyPi-url]
- [![Behave][Behave]][Behave-url]
- [![NumPy][Numpy.js]][Numpy-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started <a name="getting-started"></a>

To get a local copy up and running follow these steps.

### Prerequisites <a name="prerequisites"></a>

This list things you need to use the software and how to install them.

* using pip
  ```sh
   pip install -r requirements.txt
  ```

### Installation <a name="installation"></a>

1. Clone the repo
   ```sh
   git clone https://github.com/mournival/raytracerchallenge-py.git
   ```
2. Install PyPi packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the ray tracer
   ``` sh
   python -i input_file -o output_file
    ```
4. To run the tests (ignoring unimplemented tests), add the
    ``` sh
   --tags=-skip
   ```
   to the run command for you features test (however behave is invoked)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage <a name="usage"></a>

**TODO**
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos
work well in this space. You may also link to more resources.

   ``` sh
   python -i input_file -o output_file
   ```

[//]: # (_For more examples, please refer to the [Documentation]&#40;https://example.com&#41;_)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap <a name="roadmap"></a>

- [x] README.md
- [ ] Restart from layoff
    - [ ] Determine restart point
- ...

See the [open issues](https://github.com/mournival/raytracerchallenge-py/issues) for a full list of proposed features (
and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing <a name="contributing"></a>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->

## License <a name="license"></a>

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->

## Contact <a name="contact"></a>

Kristian Holvoet - kwh@mournival.com

Project Link: [https://github.com/mournival/raytracerchallenge-py](https://github.com/mournival/raytracerchallenge-py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->

## Acknowledgments <a name="acknowledgments"></a>

* [Jamis Buck](http://raytracerchallenge.com/) For writing [The Ray Tracer Challenge](http://raytracerchallenge.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/mournival/raytracerchallenge-py.svg?style=for-the-badge

[contributors-url]: https://github.com/mournival/raytracerchallenge-py/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/mournival/raytracerchallenge-py.svg?style=for-the-badge

[forks-url]: https://github.com/mournival/raytracerchallenge-py/network/members

[stars-shield]: https://img.shields.io/github/stars/mournival/raytracerchallenge-py.svg?style=for-the-badge

[stars-url]: https://github.com/mournival/raytracerchallenge-py/stargazers

[issues-shield]: https://img.shields.io/github/issues/mournival/raytracerchallenge-py.svg?style=for-the-badge

[issues-url]: https://github.com/mournival/raytracerchallenge-py/issues

[license-shield]: https://img.shields.io/github/license/mournival/raytracerchallenge-py.svg?style=for-the-badge

[license-url]: https://github.com/mournival/raytracerchallenge-py/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/kristian-holvoet-10101

[product-screenshot]: images/logo.png

[Behave]: https://behave.readthedocs.io/en/latest/_static/behave_logo1.png

[Behave-url]: https://behave.readthedocs.io/en/latest/

[Numpy.js]: https://numpy.org/doc/stable/_static/numpylogo.svg

[Numpy-url]: https://numpy.org/

[PyPi]:https://pypi.org/static/images/logo-small.2a411bc6.svg

[PyPi-url]:https://img.shields.io/pypi/pyversions/numpy
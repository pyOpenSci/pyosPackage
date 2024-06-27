# Publish your docs - readthedocs

There are a few ways to publish your documentation:

## ReadTheDocs

You can use ReadTheDocs. ReadTheDocs is a free to open source platform that publishes documentation. The nice thing about readthedocs is once it is setup it provides:
    *Pull request previews of your build docs
    * versioning for your built docs
    * and more

    The only downside of this platform is that if you use the free plan, your documentation with have some (ethically sourced) ads. Ads are required to support readthedocs costs in hosting documentation.

## GitHub pages

You could also use GitHub pages and create a GitHub action that pushes you documentation to the branch where github pages builds. If you use your own hosting,
    *You will loose access to the versioning that readthedocs provides and alternative outputs such as PDF.
    * You will need to build your own CI workflow to preview docs. Many use CircleCI to do this given they have a browser based html artifact feature.

There is no right or wrong answer here. However, in this demo package we use ReadTheDocs as it's the simplest, most robust approach to get your docs online quickly!

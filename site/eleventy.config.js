import { eleventyImageTransformPlugin } from "@11ty/eleventy-img";
import fs from "fs";
import yaml from "js-yaml";
import path from "path";

export default async function (eleventyConfig) {
    const prefix = "/literatura-us-redesign"; // Store this in a variable for reuse

    eleventyConfig.addPassthroughCopy("src/assets/js");
    // Note: If Image plugin outputs to assets/images, 
    // you don't need to passthrough copy the source folder.

    eleventyConfig.addPlugin(eleventyImageTransformPlugin, {
        widths: [400, 800, 1200, null],
        formats: ["webp", "jpeg"],
        outputDir: "./_site/assets/images",
        urlPath: `${prefix}/assets/images`, // Use the prefix here
        defaultAttributes: {
            loading: "lazy",
            decoding: "async",
            sizes: "100vw",
        },
    });

    eleventyConfig.addCollection("authors", function (collectionApi) {
        const dataPath = path.resolve("src/_data/authors.yaml");
        if (fs.existsSync(dataPath)) {
            const authorsData = yaml.load(fs.readFileSync(dataPath, "utf8"));
            return authorsData.map(author => ({
                ...author,
                // Root-relative URLs, the | url filter will prepends pathPrefix
                url: `/content/authors/${author.slug}/index.html`
            }));
        }
        return [];
    });

    //This prevents 11ty from outputing as index.html a file named the same as its folder, eg: cera/cera.md to cera/index.html
    //This way preventing the conflict with the file that outputs from cera/index.md to cera/index.html
    eleventyConfig.addGlobalData("permalink", "{{ page.filePathStem }}.html");

    eleventyConfig.addCollection("works", function (collectionApi) {
        const dataPath = path.resolve("src/_data/works.yaml");
        if (fs.existsSync(dataPath)) {
            const worksData = yaml.load(fs.readFileSync(dataPath, "utf8"));
            if (!Array.isArray(worksData)) return [];
            return worksData.map(work => ({
                ...work,
                // Root-relative URLs, the | url filter will prepends pathPrefix
                url: `/content/authors/${work.tags[1]}/${work.slug}.html`
            }));
        }
        return [];
    });

    return {
        pathPrefix: "/literatura-us-redesign/",
        dir: {
            input: "src",
            output: "_site",
            includes: "_includes",
            layouts: "_layouts",
        },
    };
};

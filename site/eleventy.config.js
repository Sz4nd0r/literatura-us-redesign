import { eleventyImageTransformPlugin } from "@11ty/eleventy-img";
import fs from "fs";
import yaml from "js-yaml";
import path from "path";

export default async function (eleventyConfig) {
    // Copy static assets to the output folder
    eleventyConfig.addPassthroughCopy("src/assets");

    // Register the Image Transform Plugin
    eleventyConfig.addPlugin(eleventyImageTransformPlugin, {
        // Optional: Customize widths, formats, and quality
        widths: [400, 800, 1200, null], // 'null' keeps original width
        formats: ["webp", "jpeg"],
        outputDir: "./_site/assets/images",

        // Default HTML attributes for transformed <img> tags
        defaultAttributes: {
            loading: "lazy",
            decoding: "async",
            sizes: "100vw",
        },
    });

    // Add authors collection from YAML data
    eleventyConfig.addCollection("authors", function (collectionApi) {
        const dataPath = path.resolve("src/_data/authors.yaml");
        if (fs.existsSync(dataPath)) {
            const fileContents = fs.readFileSync(dataPath, "utf8");
            const authorsData = yaml.load(fileContents);
            // Return as flat objects with a 'url' property to match template usage
            return authorsData.map(author => ({
                ...author,
                url: `/content/authors/${author.slug}/`
            }));
        }
        return [];
    });

    // Add works collection from YAML data
    eleventyConfig.addCollection("works", function (collectionApi) {
        const dataPath = path.resolve("src/_data/works.yaml");
        if (fs.existsSync(dataPath)) {
            const fileContents = fs.readFileSync(dataPath, "utf8");
            const worksData = yaml.load(fileContents);

            if (!Array.isArray(worksData)) return [];

            return worksData.map(work => ({
                ...work,
                url: `/content/authors/${work.tags[1]}/${work.slug}/`
            }));
        }
        return [];
    });

    eleventyConfig.addGlobalData("permalink", "{{ page.filePathStem }}.html");

    return {
        dir: {
            input: "src",
            output: "_site",
            includes: "_includes",
            layouts: "_layouts",
        },
    };
};

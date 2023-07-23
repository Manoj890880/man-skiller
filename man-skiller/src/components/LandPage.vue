<template>
    <nav>
        <div class="nav-container">
            <div class="logo">Man Skiller</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#sections">Sections</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#news">News</a></li>
                <li><a href="#contact">Contact Us</a></li>
                <!-- <li><a href="#login">Log In</a></li> -->
                <router-link to="/log-in">Log in</router-link>
                <router-link to="/sign-up">Sign Up</router-link>
            </ul>
        </div>
    </nav>

    <div class="banner-top">
        <div class="banner-text">
            <h1>Live Your Life with Passion and Dreams</h1>
            <!-- <p>Meet Dexam Highly customizable Pure VueJS + Bootstrap 4 Landing Pages.</p>
            <p>Minimal, Intuitive and Fully Responsive Design</p>
            <p>Super Flexible And Customizable</p> -->
            <div class="cta-buttons">
                <a href="#login">Log In</a>
                <a href="#signup">Sign Up</a>
            </div>
        </div>
    </div>

    <section class="features-section">
        <div class="container">
            <h2>Some Awesome Features</h2>
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. At velit unde cupiditate recusandae, neque
                dicta nisi omnis voluptates.</p>
        </div>
    </section>

    <section class="benefits-section">
        <div class="container">
            <h2>Benefits</h2>
            <p>Lorem ipsum dolor, sit amet consectetur. Lorem ipsum dolor, sit amet consectetur.</p>
        </div>
    </section>

    <section class="design-section">
        <div class="container">
            <h2>Design</h2>
            <p>Lorem ipsum dolor, sit amet consectetur. Lorem ipsum dolor, sit amet consectetur.</p>
        </div>
    </section>
    <!-- Rest of your website content goes here -->
</template>

<script>
export default {
    name: "LandPage",
}

</script>

<style scoped>
template {
    /* margin: 0;
    padding: 0;
    font-family: Nunito, sans-serif;
    font-size: 0.813rem;
    font-weight: 400;
    color: #fff;
    text-align: left;
    background-color: #fffafa; */
}

nav {
    background-color: #7cc871;
    padding: 15px 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.logo {
    width: auto;
    font-size: 24px;
    font-weight: bold;
    color: #000000;
}

.nav-links {
    list-style: none;
    display: flex;
    align-items: center;
    margin: 0;
    padding: 0;
}

.nav-links li {
    margin-left: 20px;
}

.nav-links li:first-child {
    margin-left: 0;
}

.nav-links a {
    color: #000000;
    text-decoration: none;
    font-size: 16px;
    padding: 8px 12px;
    border-radius: 4px;
    transition: background-color 0.2s ease;
}

.nav-links a:hover {
    background-color: #555;
}

.banner-top {

    /* background-color: #cfb6b6; */
    height: 400px;
    color: #fff;
    text-align: center;
    padding: 40px 0;
    background-image: url('http://dexam-vue.ui-lib.com/img/v3-header.635efe8e.svg');
    background-size: cover;
    background-blend-mode: darken;
}

.banner-text h1 {
    font-size: 36px;
    margin-bottom: 20px;
    color: #a47f7f;
}

.banner-text p {
    font-size: 18px;
    margin-bottom: 30px;
    color: #000;
}

.cta-buttons a {
    margin-left: 20px;
    text-align: left;
    margin-top: 300px;
    color: #555;
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    text-align: center;
    text-decoration: none;
    border-radius: 4px;
    cursor: pointer;
    background-color: #6dc4d5;
    transition: background-color 0.3s ease, color 0.3s ease, box-shadow 0.3s ease;
}

.cta-buttons a:last-child {
    margin-right: 20px;
}

.cta-buttons a:hover {
    background-color: #18afcd;
}

/* Existing CSS styles */

/* Additional styles for the new sections */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

.features-section,
.benefits-section,
.design-section {
    background-color: #f0f0f0;
    text-align: center;
}

.features-section h2,
.benefits-section h2,
.design-section h2 {
    font-size: 28px;
    margin-bottom: 20px;
}

.features-section p,
.benefits-section p,
.design-section p {
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 20px;
}

.container {
    margin-top: 40px;
}

h2.font-weight-bold {
    font-size: 28px;
    margin-bottom: 20px;
}

p {
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 20px;
}

.benefits-contents {
    align-items: center;
}

.benefits-contents i {
    font-size: 28px;
    margin-right: 10px;
}

.benefits-contents__info .card-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 5px;
}

.text-15 {
    font-size: 15px;
}

.benefits-left-img img {
    max-width: 100%;
}

/* Additional styles for responsiveness */
@media (max-width: 767px) {

    .col-lg-5,
    .offset-lg-1 {
        text-align: center;
        margin-bottom: 30px;
    }
}

/* ... Your previous CSS styles ... */

/* Additional styles for background icons */
.features-section {
    background-position: center;
    background-size: cover;
}

.benefits-section {
    background-position: center;
    background-size: cover;
}

.design-section {
    background-position: center;
    background-size: cover;
}

/* Additional styles for background icons */
.features-section:before {
    content: "";
    /* background-image: url('path/to/your/icon.svg'); */
    background-repeat: no-repeat;
    background-size: 100px;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 100px;
}

.benefits-section:before {
    content: "";
    /* background-image: url('path/to/your/icon.svg'); */
    background-repeat: no-repeat;
    background-size: 100px;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 100px;
}

.design-section:before {
    content: "";
    /* background-image: url('path/to/your/icon.svg'); */
    background-repeat: no-repeat;
    background-size: 100px;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 100px;
}

.features-section {
    /* background-image: url('path/to/your/image1.jpg'); */
    background-color: #ffccaa;
    background-blend-mode: multiply;
    background-position: center;
    background-size: cover;
}

.benefits-section {
    /* background-image: url('path/to/your/image2.jpg'); */
    background-color: #aaffdd;
    background-blend-mode: multiply;
    background-position: center;
    background-size: cover;
}

.design-section {
    /* background-image: url('path/to/your/image3.jpg'); */
    background-color: #ffddee;
    background-blend-mode: multiply;
    background-position: center;
    background-size: cover;
}

/* Additional styles for background icons */
.features-section:before,
.benefits-section:before,
.design-section:before {
    content: "";
    /* background-image: url('path/to/your/icon.svg'); */
    background-repeat: no-repeat;
    background-size: 100px;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 100px;
    opacity: 0.5;
    filter: brightness(2) saturate(2);
}
</style>
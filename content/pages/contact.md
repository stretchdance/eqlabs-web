Title: Contact
Date: 2020-06-14
Category: Basics
pageindex: 4
illustration: contactheader.jpg
backurl: /images/back.svg
headersubtitle: We'd love to hear from you
headertitle: Get in touch

<form data-netlify="true" name="contact" method="POST">

<div class="row">
    <div class="col d-flex flex-column justify-content-around" style="min-height: 60vh;">

        <h1 class="main-title">We would be delighted to hear from you.</h1>
        <div>
        <b>Email</b><br/>
        <a href="mailto:discovery@eqlabs.io">discovery@eqlabs.io</a>
        </div>

        <div>
        <b>Phone</b><br/>
        <a href="tel:+1-250-434-5773">+1-250-434-5773</a>
        </div>

        <div>
        <b>Address</b><br/>
        <a href="maps://?q=4326+3rd+Ave+NW,+Seattle,+WA,+98107">4326 3rd Ave NW, Seattle, WA, 98107</a>
        </div>

    </div>
    <div class="col align-self-end">


        <div class="form-group">
            <label for="exampleInputName1">Name</label>
            <input type="name" name="fullname" class="form-control" id="exampleInputName1" aria-describedby="nameHelp" placeholder="Full name">
            <small id="nameHelp" class="form-text text-muted">How should we address you?</small>
        </div>

        <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" name="emailaddress" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
        </div>

        <div class="form-group">
            <label for="exampleFormControlTextarea1">Message</label>
            <textarea class="form-control" name="message" id="exampleFormControlTextarea1" rows="5"></textarea>
        </div>

    </div>
</div>

<div class="row mb-5">
    <div class="col offset-6">
        <div class="form-group text-center">
            <button type="submit" class="btn btn-primary blue-button">Send Message</button>
        </div>
    </div>
</div>

</form>
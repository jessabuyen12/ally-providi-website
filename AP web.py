from zipfile import ZipFile
import os

base_dir = "/mnt/data/ally_providi_premium_website"
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ally Providi BPO | Premium Outsourcing Solutions</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="style.css">

<meta name="description" content="Ally Providi BPO - Premium outsourcing solutions in the Philippines. Customer support, data entry, sales, HR outsourcing and more.">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

</head>

<body>

<!-- NAV -->
<nav class="navbar navbar-expand-lg navbar-dark fixed-top glass">
  <div class="container">
    <a class="navbar-brand fw-bold" href="#">ALLY PROVIDI</a>
    <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#nav">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="nav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
        <li class="nav-item"><a class="nav-link" href="#services">Services</a></li>
        <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
      </ul>
    </div>
  </div>
</nav>

<!-- HERO -->
<header id="home" class="hero d-flex align-items-center text-center text-white">
  <div class="container">
    <h1 class="display-4 fw-bold animate">Reliable Outsourcing. Real Results.</h1>
    <p class="lead">Premium BPO Solutions Built for Growth</p>
    <a href="#contact" class="btn btn-warning btn-lg mt-3">Get a Quote</a>
  </div>
</header>

<!-- ABOUT -->
<section id="about" class="section">
  <div class="container">
    <h2 class="title">About Us</h2>
    <p>
      Ally Providi BPO is a Philippines-based outsourcing company providing scalable business solutions.
      We help businesses reduce cost, improve efficiency, and scale operations through expert remote teams.
    </p>
  </div>
</section>

<!-- SERVICES -->
<section id="services" class="section bg-light">
  <div class="container">
    <h2 class="title text-center">Our Services</h2>

    <div class="row g-4 mt-3">
      <div class="col-md-4"><div class="card premium">Customer Support</div></div>
      <div class="col-md-4"><div class="card premium">Data Entry & Processing</div></div>
      <div class="col-md-4"><div class="card premium">Telemarketing & Sales</div></div>
      <div class="col-md-4"><div class="card premium">Technical Support</div></div>
      <div class="col-md-4"><div class="card premium">HR Outsourcing</div></div>
      <div class="col-md-4"><div class="card premium">Accounting Support</div></div>
    </div>
  </div>
</section>

<!-- WHY US -->
<section class="section">
  <div class="container text-center">
    <h2 class="title">Why Choose Us</h2>

    <div class="row mt-4">
      <div class="col-md-4">✔ We Build Long-Term Partnerships</div>
      <div class="col-md-4">✔ We Deliver Measurable Results</div>
      <div class="col-md-4">✔ We Provide Dedicated Support</div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="section bg-light">
  <div class="container text-center">
    <h2 class="title">Testimonials</h2>
    <p class="mt-3">“Professional and reliable outsourcing partner.”</p>
    <p>- Client Feedback</p>
  </div>
</section>

<!-- CONTACT -->
<section id="contact" class="section">
  <div class="container">
    <h2 class="title text-center">Contact Us</h2>

    <form class="row g-3 mt-3">
      <div class="col-md-6"><input class="form-control" placeholder="Name"></div>
      <div class="col-md-6"><input class="form-control" placeholder="Email"></div>
      <div class="col-12"><textarea class="form-control" rows="5" placeholder="Message"></textarea></div>
      <div class="col-12 text-center">
        <button class="btn btn-warning btn-lg">Send Inquiry</button>
      </div>
    </form>

    <div class="text-center mt-4">
      <p>📞 +63 960 849 7629</p>
      <p>📧 partners@allyprovidi.com</p>
    </div>
  </div>
</section>

<!-- FLOAT BUTTONS -->
<a class="messenger" href="https://m.me/allyprovidi">💬 Messenger</a>
<a class="whatsapp" href="https://wa.me/639608497629">📱 WhatsApp</a>

<footer class="footer text-center">
© 2026 Ally Providi BPO. All Rights Reserved.
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="script.js"></script>

</body>
</html>
"""

style_css = """
body{
font-family: Inter, sans-serif;
scroll-behavior:smooth;
}

.glass{
background: rgba(0,0,0,0.7);
backdrop-filter: blur(10px);
}

.hero{
height:100vh;
background: linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.6)),
url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d') center/cover;
}

.section{
padding:80px 0;
}

.title{
font-weight:700;
margin-bottom:20px;
}

.premium{
padding:20px;
border-radius:12px;
transition:0.3s;
box-shadow:0 5px 20px rgba(0,0,0,0.1);
}

.premium:hover{
transform:translateY(-5px);
}

.messenger,.whatsapp{
position:fixed;
right:20px;
padding:12px 15px;
border-radius:50px;
text-decoration:none;
color:#fff;
font-weight:600;
}

.messenger{bottom:90px;background:#0084ff;}
.whatsapp{bottom:30px;background:#25D366;}

.footer{
background:#111;
color:#fff;
padding:20px;
}
"""

script_js = """
console.log("Premium Ally Providi Website Loaded");
"""

with open(os.path.join(base_dir, "index.html"), "w") as f:
    f.write(index_html)

with open(os.path.join(base_dir, "style.css"), "w") as f:
    f.write(style_css)

with open(os.path.join(base_dir, "script.js"), "w") as f:
    f.write(script_js)

zip_path = "/mnt/data/ally_providi_premium_website.zip"
with ZipFile(zip_path, "w") as zipf:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, base_dir)
            zipf.write(file_path, arcname)

zip_path

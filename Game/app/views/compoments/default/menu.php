<div class="bs-example">
    <nav class="navbar navbar-expand-md bg-dark navbar-dark">
        <a href="#" class="navbar-brand">
            <img src="<?php print(imgPath); ?>logo.png" alt="Quiz" class="menuLogo" />
        </a>
        <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse justify-content-between" id="navbarCollapse">
            <div class="navbar-nav">
                <?php if(!isset($_SESSION['user'])){ ?>
                    <a href="/login" class="nav-item nav-link active">Login</a>
                    <a href="/registration" class="nav-item nav-link">Registration</a>
                <?php } else { ?> 
                    <a href="/highscore" class="nav-item nav-link">High score</a>
                    <a href="/quiz" class="nav-item nav-link">Quiz</a>
                    <a href="/logout" class="nav-item nav-link">Logout</a>
                <?php } ?>
            </div>  
        </div>
    </nav>
</div>
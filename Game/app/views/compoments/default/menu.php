<div class="bs-example">
    <nav class="navbar navbar-expand-md bg-dark navbar-dark">
        <a href="/home" class="navbar-brand">
            <img src="<?php print(imgPath); ?>logo.png" alt="Quiz" class="menuLogo" />
        </a>
        <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse justify-content-between" id="navbarCollapse">
            <div class="navbar-nav">
                <?php if(!isset($_SESSION['username'])){ ?>
                    <a href="/user/login" class="nav-item nav-link active">Login</a>
                    <a href="/user/registration" class="nav-item nav-link">Registration</a>
                <?php } else { ?> 
                    <a href="/highscore/show" class="nav-item nav-link">High score</a>
                    <a href="/game/quiz" class="nav-item nav-link">Quiz</a>
                    <a href="/user/logout" class="nav-item nav-link">Logout</a>
                <?php } ?>
            </div>  
        </div>
    </nav>
</div>
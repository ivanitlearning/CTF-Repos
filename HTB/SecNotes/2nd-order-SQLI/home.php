<?php
$includes = 1;
require_once 'auth.php';
require_once 'db.php';

if (isset($_SESSION['home-error'])) {
    $general_error = $_SESSION['home-error'];
} else {
    $general_error = "Due to GDPR, all users must delete any notes that contain Personally Identifable Information (PII)<br/>Please contact <strong>tyler@secnotes.htb</strong> using the contact link below with any questions.";
}
unset($_SESSION['home-error']);

// if delete, delete post
if ($_REQUEST['action'] = 'delete' and isset($_REQUEST["id"])) {
    $sql = "DELETE FROM posts WHERE username = ? and id = ?";
    if($stmt = mysqli_prepare($link, $sql)) {
        mysqli_stmt_bind_param($stmt, "ss", $param_username, $param_id);
        $param_username = $username;
        $param_id = $_REQUEST['id'];
        mysqli_stmt_execute($stmt);
        if(mysqli_stmt_execute($stmt)){
            $general_error = "Note deleted.";
        } else {
            $general_error = $link->error;
        }
    } else {
        $general_error = $link->error;
    }
    $_SESSION['home-error'] = $general_error;
    header("location: home.php");
}
?>
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure Notes - Home</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
    <style type="text/css">
        body{ font: 14px sans-serif; text-align: center; }
        .accordion {
            background-color: #eee;
            color: #444;
            cursor: pointer;
            padding: 18px;
            width: 80%;
            border: none;
            text-align: left;
            outline: none;
            font-size: 15px;
            transition: 0.4s;
        }

        .active, .accordion:hover {
            background-color: #ccc;
        }

        .accordion:after {
            content: '\002B';
            color: #777;
            font-weight: bold;
            float: right;
            margin-left: 5px;
        }

        .active:after {
            content: "\2212";
        }

        .panel {
            padding: 0 18px;
            background-color: white;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.2s ease-out;
        }
    </style>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</head>
<body>
    <div class="alert alert-warning">
      <?php echo $general_error; ?>
    </div>
    <div class="page-header">
        <h1>Viewing Secure Notes for <b><?php echo htmlspecialchars($username); ?></b></h1>
    </div>
    <div>
    <?php
    $sql = "SELECT id, title, note, created_at FROM posts WHERE username = '" . $username . "'";
    $res = mysqli_query($link, $sql);
    if (mysqli_num_rows($res) > 0) {
        while ($row = mysqli_fetch_row($res)) { 
            echo '<button class="accordion"><strong>' . $row[1] . '</strong>  <small>[' . $row[3] . ']</small></button>';
            echo '<a href=/home.php?action=delete&id=' . $row[0] . '" class="btn btn-danger"><strong>X</strong></a>';
            echo '<div class="panel center-block text-left" style="width: 78%;"><pre>' . $row[2] . '</pre></div>';
        }
    } else {
        echo '<p>User <strong>' . $username . '</strong> has no notes. Create one by clicking below.</p>';
    }
    ?>
    </div>
    <div class="btn-group">
    <a href="submit_note.php" class="btn btn-lg btn-block btn-success">New Note</a>
    <a href="change_pass.php" class="btn btn-lg btn-block btn-warning">Change Password</a>
    <a href="logout.php" class="btn btn-lg btn-block btn-danger">Sign Out</a>
    <a href="contact.php" class="btn btn-lg btn-block btn-info">Contact Us</a>
    </div>
    

    
    <script>
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling.nextElementSibling;
        if (panel.style.maxHeight){
          panel.style.maxHeight = null;
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        } 
      });
    }
    </script>
</body>
</html>
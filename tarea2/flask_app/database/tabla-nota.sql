-- Active: 1795381986461@@127.0.0.1@3306@tarea2
CREATE TABLE IF NOT EXISTS `tarea2`.`nota` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `avistamiento_id` INT NOT NULL,
  `nota` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_nota_avistamiento1_idx` (`avistamiento_id` ASC),
  CONSTRAINT `fk_nota_avistamiento1`
    FOREIGN KEY (`avistamiento_id`)
    REFERENCES `tarea2`.`avistamiento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

package tarea4.tarea4.controllers;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import tarea4.tarea4.services.AppService;

@Controller
public class AppController {
     private final AppService appService;
    public AppController(AppService appService) {
        this.appService = appService;
    }

    @GetMapping("/")
    public String indexRoute(Model model) {
        List<Map<String, String>> modelData = appService.getAvistamientosData(3);
        model.addAttribute("data", modelData);
        return "tarea4";
    }

    @PostMapping("/post-avis")
    public String postConfRoute(
        @RequestParam("nombre") String nombre,
        @RequestParam("dia") LocalDateTime dia,
        @RequestParam("ave") String ave,
        @RequestParam("comuna") String comuna) throws Exception {
        
        appService.handlePostRequest(
            nombre,
            dia,
            ave,
            comuna
        );

        return "redirect:/"; //redirects to indexRoute
    }



}

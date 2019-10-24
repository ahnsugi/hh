package koreatech.cse.controller;

import koreatech.cse.domain.H2member;
import koreatech.cse.repository.H2memberMapper;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import javax.inject.Inject;

@Controller
@RequestMapping("/hh")
public class H2Controller {
    @Inject
    H2memberMapper h2memberMapper;

    @RequestMapping("/about")
    public String home(Model model, @RequestParam(required=false) String name) {
        String ceo_name = "Mr.Ahn";
        if(name != null){
             ceo_name = name;
        }

        model.addAttribute("ceoName",ceo_name);
        return "hh/about";
    }

    @RequestMapping("/blog/{id}")
    public String blog(Model model,
                       @PathVariable(value = "id") String id) {

        model.addAttribute("blogId",id);
        return "hh/blog";
    }

    @RequestMapping("/signup")
    public String signup(Model model) {
        H2member h2member = new H2member();
        model.addAttribute("h2member",h2member);

        return "hh/signup";
    }

    @RequestMapping(value="/signup", method= RequestMethod.POST)
    public String signup(@ModelAttribute H2member h2member) {
        System.out.println(h2member.getName());
        h2memberMapper.insert(h2member);
        return "redirect:/hh/about";
    }
}

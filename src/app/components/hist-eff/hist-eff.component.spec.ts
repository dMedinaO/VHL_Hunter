import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistEffComponent } from './hist-eff.component';

describe('HistEffComponent', () => {
  let component: HistEffComponent;
  let fixture: ComponentFixture<HistEffComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HistEffComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HistEffComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
